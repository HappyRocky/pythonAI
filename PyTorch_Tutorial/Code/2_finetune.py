# -*- coding: utf-8 -*-
import torch
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
import numpy as np
import os
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
from torch import optim
from utils.utils import MyDataset, validate, show_confMat
from datetime import datetime

train_txt_path = os.path.join("..", "Data", "train.txt")
valid_txt_path = os.path.join("..", "Data", "valid.txt")

classes_name = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

train_bs = 16
valid_bs = 16
lr_init = 0.001
max_epoch = 5

# log
result_dir = os.path.join("..", "Result")

now_time = datetime.now()
time_str = datetime.strftime(now_time, '%m-%d_%H-%M-%S')

log_dir = os.path.join(result_dir, time_str)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# -------------------------------------------- step 1/5 : 加载数据 -------------------------------------------

# 数据预处理设置
normMean = [0.4948052, 0.48568845, 0.44682974]
normStd = [0.24580306, 0.24236229, 0.2603115]
normTransform = transforms.Normalize(normMean, normStd)
trainTransform = transforms.Compose([
    transforms.Resize(32),
    transforms.RandomCrop(32, padding=4),
    transforms.ToTensor(),
    normTransform
])

validTransform = transforms.Compose([
    transforms.ToTensor(),
    normTransform
])

# 构建MyDataset实例
train_data = MyDataset(txt_path=train_txt_path, transform=trainTransform)
valid_data = MyDataset(txt_path=valid_txt_path, transform=validTransform)

# 构建DataLoder
train_loader = DataLoader(dataset=train_data, batch_size=train_bs, shuffle=True)
valid_loader = DataLoader(dataset=valid_data, batch_size=valid_bs)

# ------------------------------------ step 2/5 : 定义网络 ------------------------------------


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool1(F.relu(self.conv1(x)))
        x = self.pool2(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    # 定义权值初始化
    def initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                torch.nn.init.xavier_normal_(m.weight.data)
                if m.bias is not None:
                    m.bias.data.zero_()
            elif isinstance(m, nn.BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
            elif isinstance(m, nn.Linear):
                torch.nn.init.normal_(m.weight.data, 0, 0.01)
                m.bias.data.zero_()


net = Net()     # 创建一个网络

# ================================ #
#        finetune 权值初始化
# ================================ #

pretrained_dict = torch.load('../Result/06-03_23-03-06/net_params.pkl')

net_state_dict = net.state_dict()

pretrained_dict_1 = {k:v for k,v in pretrained_dict.items() if k in net_state_dict}

net_state_dict.update(pretrained_dict_1)

net.load_state_dict(net_state_dict)
# ------------------------------------ step 3/5 : 定义损失函数和优化器 ------------------------------------
# ================================= #
#         按需设置学习率
# ================================= #

ignored_params = list(map(id, net.fc3.parameters()))
base_params = filter(lambda p: id(p) not in ignored_params, net.parameters())

optimizer = optim.SGD(
    [
        {'params': base_params},
        {'params': net.fc3.parameters(), 'lr': lr_init * 10}
    ],
    lr_init,
    momentum=0.9,
    weight_decay=1e-4
)

criterion = nn.CrossEntropyLoss()
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=50, gamma=0.1)

# ------------------------------------ step 4/5 : 训练 --------------------------------------------------

for epoch in range(max_epoch):

    loss_sigma = 0.0
    correct = 0.0
    total = 0.0

    for i, data in enumerate(train_loader):

        # 获取数据
        inputs, labels = data
        inputs, labels = Variable(inputs), Variable(labels)

        # 执行一次前馈和回馈
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # 统计预测信息
        _, predicted = torch.max(outputs.data, 1)  # 返回二维元组，第一个是最大值，第二个是最大值的索引
        total += labels.size(0)
        correct += (predicted == labels).squeeze().sum().numpy()
        loss_sigma += loss.item()

        if i % 10 == 9:
            loss_avg = loss_sigma / 10
            loss_sigma = 0.0
            print('Training: Epoch[{:0>3}/{:0>3}] Iteration[{:0>3}/{:0>3}] Loss:{:.4f} Acc:{:.2%}'.format(
                epoch + 1, max_epoch, i + 1, len(train_loader), loss_avg, correct / total
            ))
            print('参数组1的学习率:{}, 参数组2的学习率:{}'.format(scheduler.get_lr()[0], scheduler.get_lr()[1]))

    # 观察模型在验证集的表现
    loss_sigma = 0.0
    cls_num = len(classes_name)
    conf_mat = np.zeros([cls_num, cls_num])
    net.eval()
    for i, data in enumerate(valid_loader):
        images, labels = data
        images, labels = Variable(images), Variable(labels)

        outputs = net(images)
        outputs.detach_()

        loss = criterion(outputs, labels)
        loss_sigma += loss.item()

        _, predicted = torch.max(outputs.data, 1)

        for j in range(len(labels)):
            conf_mat[labels[j].numpy(), predicted[j].numpy()] += 1.0

    print('valid set Acc:{:.2%}'.format(conf_mat.trace() / conf_mat.sum()))

    scheduler.step()  # 更新学习率

print('Finished Training')

# ------------------------------------ step5: 保存模型 并且绘制混淆矩阵图 ------------------------------------
conf_mat_train, train_acc = validate(net, train_loader, 'train', classes_name)
conf_mat_valid, valid_acc = validate(net, valid_loader, 'valid', classes_name)

show_confMat(conf_mat_train, classes_name, 'train', log_dir)
show_confMat(conf_mat_valid, classes_name, 'valid', log_dir)

# -*- coding: utf-8 -*-

'''
pytorch版本：0.4
实现一个demo，对torch自带的minist手写数据集进行cnn分类
'''

import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.utils.data as Data
import torchvision

# 设置生成随机数的种子
torch.manual_seed(1)

EPOCH = 1
BATCH_SIZE = 50

class CNN(nn.Module): # 网络结构，继承 Module
    def __init__(self):
        
        # super 的工作原理：
        # 先找到 CNN 的父类，即 nn.Module
        # 然后把 CNN 的对象 self 转换成 nn.Module
        # 然后转换之后的对象调用自己的 __init__函数
        super(CNN, self).__init__() # 调用父类的__init__
        self.conv1 = nn.Sequential(nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5, stride=1, padding=2), # (16,28,28)
                                   nn.ReLU(),
                                   nn.MaxPool2d(kernel_size=2))
        self.conv2 = nn.Sequential(nn.Conv2d(16, 32, 5, 1, 2),
                                   nn.ReLU(),
                                   nn.MaxPool2d(2))
        self.out = nn.Linear(32*7*7, 10)
        
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)# 将（batch，32,7,7）展平为（batch，32*7*7）
        output = self.out(x)
        return output
    
def getData(): # 获取数据
    training_data = torchvision.datasets.MNIST(
            root = './mnist/', # dataset存储路径
            train=True, # True表示是train训练集，False表示test测试集
            transform=torchvision.transforms.ToTensor(), # 将原数据规范化到01之间
            download=False # 获取训练集dataset
            )
    train_loader = Data.DataLoader(dataset=training_data, 
                                   batch_size=BATCH_SIZE,
                                   shuffle=True) # dataset格式可直接放入DataLoader
    test_data = torchvision.datasets.MNIST(root='./mnist/',train=False) # 获取测试集
    test_x = Variable(torch.unsqueeze(test_data.test_data, dim=1)).type(torch.FloatTensor)[:20]/255 # 取前2000个测试样本
    # torch.unsqueeze(x,dim):增加维度，假如x的大小为 (2,4)，将 (2,4) 看成一个数组，dim表示即将插入的值为1的索引位置
    # 比如 dim=0，则将 1 插入到索引 0 的位置上，变成 (1,2,4)，返回 1*2*4 的三维的数据。每个数据的值是不变的。
    test_y = test_data.test_labels[:20]
    return train_loader, test_x, test_y

def trainModel(): # 训练模型
    train_loader, test_x, test_y = getData()
    model = CNN()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)    
    loss_function = nn.CrossEntropyLoss()
    
    for epoch in range(EPOCH):
        for step, (x, y) in enumerate(train_loader):
            output = model(x)
            loss = loss_function(output, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            if step % 100 == 0:
                test_output = model(test_x)
                pred_y = torch.max(test_output, 1)[1].data.squeeze()
                accuracy = float(sum(pred_y == test_y)) / test_y.size(0)
                print(f'Epoch:{epoch}, Step:{step}, Train loss:{loss.item()}, test acc:{accuracy}')
                print(f'pred_y:{pred_y.numpy()}')
                print(f'test_y:{test_y.numpy()}')
    return model

if __name__ == '__main__':
    
    # 训练
    model = trainModel()
    
    # 测试
    _, tx, ty = getData()
    test_output = model(tx[:20])
    py = torch.max(test_output, 1)[1].data.numpy().squeeze()
    print(f'真实数据: {ty[:20].numpy()}')
    print(f'预测结果: {py}')
    
    


    
        
        
# 读取CIFAR10数据
import numpy as np
import pickle # save/reload功能
import sys # 负责程序与解释器的交互，如标准输入输出等

# 从一个CIFAR10文件中读取数据
def load_CIFAR10_batch(filename):
    with open(filename, 'rb') as f:
        if sys.version_info[0] < 3: # sys.version_info(major=3, minor=5, micro=2, releaselevel='final', serial=0) 版本：3.5.2
            dict = pickle.load(f)
        else:
            dict = pickle.load(f, encoding='latin1')
        x = dict['data']
        y = dict['labels']
        x = x.astype(float) # 类型转换，转换为float类型
        y = np.array(y)
    return x, y

# 读取所有CIFAR10的数据
def load_data():
    
    # 读取训练集
    xs = []
    ys = []
    for i in range(1,6):
        filename = 'F:/myPython/data/cifar-10-python/cifar-10-batches-py/data_batch_' + str(i)
        X, Y = load_CIFAR10_batch(filename)
        xs.append(X)
        ys.append(Y)
    x_train = np.concatenate(xs)
    y_train = np.concatenate(ys)
    del xs, ys
    
    # 读取测试集
    x_test, y_test = load_CIFAR10_batch('F:/myPython/data/cifar-10-python/cifar-10-batches-py/test_batch')
    
    # 十个类别
    classes = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    
    # 数据归一化
    mean_image = np.mean(x_train, axis=0)
    x_train -= mean_image
    x_test -= mean_image
    
    data_dict = {
        'images_train': x_train,
        'labels_train': y_train,
        'images_test': x_test,
        'labels_test': y_test,
        'classes': classes
    }
    return data_dict

def reshape_data(data_dict):
    im_tr = np.array(data_dict['images_train'])
    im_tr = np.reshape(im_tr, (-1, 3, 32, 32))
    im_tr = np.transpose(im_tr, (0, 2, 3, 1))
    data_dict['images_train'] = im_tr
    im_te = np.array(data_dict['images_test'])
    im_te = np.reshape(im_te, (-1, 3, 32, 32))
    im_te = np.transpose(im_te, (0,2,3,1))
    data_dict['images_test'] = im_te
    return data_dict

def gen_batch(data, batch_size, num_iter):
    data = np.array(data)
    index = len(data)
    for i in range(num_iter):
        index += batch_size
        if(index + batch_size > len(data)):
            index = 0
            shuffled_indices = np.random.permutation(np.arange(len(data)))
            data = data[shuffled_indices]
        yield data[index:index + batch_size]
        
def main():
    data_sets = load_data()
    print(data_sets['images_train'].shape)
    print(data_sets['labels_train'].shape)
    print(data_sets['images_test'].shape)
    print(data_sets['labels_test'].shape)

if __name__ == '__main__':
    main()

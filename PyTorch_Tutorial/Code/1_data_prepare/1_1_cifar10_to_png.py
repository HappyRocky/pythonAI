# -*- coding: utf-8 -*-
"""
保存cifar的图片集
"""

import matplotlib.pyplot as plt
import numpy as np
import os
import pickle

data_dir = os.path.join('..', '..', 'Data', 'cifar-10-batches-py')
train_o_dir = os.path.join("..", "..", "Data", "cifar-10-png", "raw_train")
test_o_dir = os.path.join("..", "..", "Data", "cifar-10-png", "raw_test")

Train = False  # 不解压训练集，仅解压测试集


# 解压缩，返回解压后的字典
def unpickle(file):
    with open(file, 'rb') as fo:
        dict_ = pickle.load(fo, encoding='bytes')
    return dict_


def my_mkdir(my_dir):
    if not os.path.isdir(my_dir):
        os.makedirs(my_dir)


if '__main__' == __name__:
    if Train:
        print('train_batch is loading...')
        for j in range(1, 6):
            data_path = os.path.join(data_dir, "data_batch_" + str(j))
            train_data = unpickle(data_path)
            print(data_path + " is loading...")

            for i in range(0, 10000):
                img = np.reshape(train_data[b'data'][i], (3, 32, 32))
                img = img.transpose(1, 2, 0)  # 以前的(x,y,z)坐标转置为(y,z,x)

                # 将图片分类别保存
                label_num = str(train_data[b'labels'][i])
                o_dir = os.path.join(train_o_dir, label_num)
                my_mkdir(o_dir)
                img_name = label_num + '_' + str(i + (j - 1) * 10000) + '.png'
                img_path = os.path.join(o_dir, img_name)
                plt.imsave(img_path, img)

            print(data_path + " loaded.")

    print('test_batch is loading...')
    test_data_path = os.path.join(data_dir, 'test_batch')
    test_data = unpickle(test_data_path)
    for i in range(0, 10000):
        img = np.reshape(test_data[b'data'][i], (3, 32, 32))
        img = img.transpose(1, 2, 0)  # 以前的(x,y,z)坐标转置为(y,z,x)

        # 将图片分类别保存
        label_num = str(test_data[b'labels'][i])
        o_dir = os.path.join(test_o_dir, label_num)
        my_mkdir(o_dir)
        img_name = label_num + '_' + str(i) + '.png'
        img_path = os.path.join(o_dir, img_name)
        plt.imsave(img_path, img)
    print('test_batch loaded.')


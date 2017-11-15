# 读取CIFAR10数据
import numpy as np
import pickle # save/reload功能
import sys # 负责程序与解释器的交互，如标准输入输出等

# 从一个CIFAR10文件中读取数据
def load_CIFAR10_batch(filename):
    with open(filename, 'rb')



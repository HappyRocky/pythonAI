# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import cv2
import numpy as np
import os

def get_diff(image_file, threshold = 0):
    '''
    计算一个图片的复杂程度。
    '''

    img = plt.imread(image_file)                        #在这里读取图片
    # 灰度化
    gravity = np.array([0.299,0.587,0.114])
    img = np.dot(img, gravity)
    fil = np.array([[ 1, 1, 1],                        #这个是设置的滤波，也就是卷积核
                [ 1, -8, 1],
                [ 1, 1, 1]])
    
    #fil = np.array([[ -1, 1],                        #这个是设置的滤波，也就是卷积核
    #                [ 1, -1]])

    res = cv2.filter2D(img,-1,fil)                      #使用opencv的卷积函数
    # 求平均值
    size = res.shape[0] * res.shape[1]
    if threshold == 0:
        res = abs(res)
        mean = res.sum() / size
    else:
        mean = 0    
        for i in range(res.shape[0]):
            for j in range(res.shape[1]):
                value = abs(res[i][j])
                if value >= threshold:
                    mean += value
        mean = mean / size
    return mean


if '__main__' == __name__:
    image_path = 'simple'
    file_list = os.listdir(image_path) #列出文件夹下所有的目录与文件
    diff_dict = dict()
    for file in file_list:
        full_file = os.path.join(image_path, file)
        diff = get_diff(full_file)
        diff_dict[file] = diff
        
    diff_list = sorted(diff_dict, key=lambda x : diff_dict[x])
    for file in diff_list:
        print(f'{file}\t{diff_dict[file]}')
    
    # 遍历threshold
    '''
    file1 = 'complex/2bb7442075c582ef.jpg'
    file2 = 'simple/5b712c68N2bf14ea7.jpg'
    min_th = 0
    min_diff = 999999999
    for threshold in range(1, 200, 10):
        diff_file1 = abs(get_diff(file1, threshold))
        diff_file2 = abs(get_diff(file2, threshold))
        diff = abs(diff_file1 - diff_file2)
        print(f'threshold={threshold}, diff_file1={diff_file1}, diff_file2={diff_file2}')
        if diff < min_diff:
            min_th = threshold
            min_diff = diff
    print(f'min_threshold={min_th}')
    '''
    

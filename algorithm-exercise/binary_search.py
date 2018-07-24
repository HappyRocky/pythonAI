# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 19:45:28 2018

@author: gongyanshang1

实现二分查找
"""
import random
import time
import matplotlib.pyplot as plt

def bsearch(values, target):
    '''
    在有序数组中查询是否存在等于target的元素
    values:递增数组,values[0]<=values[1]<=...
    target:待查找的元素值
    return 非负数：target在values中的位置；-1：values中不包含target
    '''
    if values[0] > target or values[-1] < target:
        return -1
    return bsearch_rec(values, target, 0)

def bsearch_rec(values, target, pre_num):
    '''
    尾递归，查询values中是否存在等于target的元素
    values:递增数组,values[0]<=values[1]<=...
    target:待查找的元素值
    pre_num:当前values在原始values中的位置
    return 非负数：target在values中的位置；-1：values中不包含target
    '''
    if values == None or len(values) == 0:
        return -1

    # 长度为1或2，则直接遍历判断
    if len(values) <= 2:
        for i in range(0, len(values)):
            if values[i] == target:
                return i + pre_num
        return -1
    
    # 取中位数，判断下次搜索是前半部分还是后半部分
    mid = round(len(values) / 2)
    if target == values[mid]:
        return mid + pre_num
    if target < values[mid]:
        return bsearch_rec(values[0:mid], target, pre_num)
    return bsearch_rec(values[mid+1:], target, pre_num+mid+1)

if '__main__' == __name__:
    
    # 验证时间复杂度为O(logn)
    times = 1000 # 随机取数的次数，方便时间取平均值
    length_list = list(range(10000, 20000)) # 数组的长度
    time_list = [0] * len(length_list)
    for i in range(0, len(length_list)):
        length = length_list[i]
        values = list(range(0, length))
        mean_time = 0
        for j in range(0, times): # 随机生成times次target，取耗费时间的平均值
            target = random.randint(values[0], values[-1])
            
            # 计算时间
            time_start = time.time()
            idx = bsearch(values, target)
            time_diff = time.time() - time_start
            
            mean_time += time_diff
        #mean_time /= times * 100000
        time_list[i] = mean_time
    plt.plot(length_list, time_list, 'r-')



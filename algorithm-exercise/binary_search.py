# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 19:45:28 2018

@author: gongyanshang1

实现二分查找
"""

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
    values = [2,4,5,6,8,12,34,44,64,65]
    target = 34
    idx = bsearch(values, target)
    if idx == -1:
        print('%d不存在于%s中' % (target, str(values)))
    else:
        print('查找成功：values[%d]=%d' % (idx, values[idx]))
    



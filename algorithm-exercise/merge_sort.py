# -*- coding: utf-8 -*-

'''
实现归并排序
'''

def merge_sort(lists):
    '''
    递归进行归并排序。
    '''
    # 递归结束条件
    if len(lists) <= 1:
        return lists
    
    # 分治进行递归
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    
    # 将两个有序数组进行合并
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # 将较小值放入到result中
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 将未被扫描到的直接追加到result后面
    if i == len(left):
        result.extend(right[j:])
    else:
        result.extend(left[i:])
    
    return result
    
if __name__ == '__main__':
    a = [2, 6, 10, 3, 5, 8, 4]
    print(merge_sort(a))
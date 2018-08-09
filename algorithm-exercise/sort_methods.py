# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:32:28 2018

@author: gongyanshang1

实现各种排序算法
"""
import matplotlib.pyplot as plt
import math
import numpy as np

def qsort1(a):
    '''
    最简单的快速排序，分治思想。
    1、随机选择一个值t，固定。
    2、从左到右扫描，最终实现数组左半边都小于t，右半边都大于等于t。
      具体方法：初始化扫描下标i=0、分界线下标m=0，算法循环中不断向右移动下标i，并适当进行交换值和右移m，以维持不变式：a[1...m]<t and a[m+1...]>=t
    3、递归 qsort1([0...m-1]) 和 qsort1([m+1...])
    '''
    count = 0
    def qsort1_rec(a, l, u):
        '''
        用于递归
        '''
        if l >= u:
            return
        
        # 初始化，将 t 定为第一个元素值
        m = l
        t = a[l]
        
        # 遍历
        for i in range(l+1, u+1): # i 始终在 m 的右边，m 始终是数组前半部分的最后一位。（前半部分都小于t，后半部分都大于等于t，前半部分不包括第一个元素a[l]，因为a[l]=t）
            nonlocal count
            count += 1
            if a[i] < t: # a[i] 在 m 右边，但是比 t 小，想办法把它弄到 m 左边去
                m += 1 # 加1之后，m不再是前半部分的最后一位，而变成了后半部分的第一位。此时 a[m] >= t。
                a[m], a[i] = a[i], a[m] # 两个位置的值互换，之前比t小的a[i]现在紧跟在前半部分的最右面，相当于前半部分的集合add了1个值， m 又变成了前半部分的最后一位，同时也有 a[i] >= t。
        
        # 最后一步，交换m和l位置。因为 t = a[l]，因此 a[l] 是最适合当分界线的。这样做之后，所有的前半部分就会都都小于t，包括第一个元素a[l]。
        a[l], a[m] = a[m], a[l]
        
        # 分别对前半部分和后半部分排序（不包括分界线a[m]）
        qsort1_rec(a, l, m-1)
        qsort1_rec(a, m+1, u)
    
    # 开始递归
    qsort1_rec(a, 0, len(a)-1)
    return count
    
    
if '__main__' == __name__:
    a = [32,1,456,234,7,23,87,123,456]
    qsort1(a)
    print(a)
    
    # 测试复杂度。结论：qsort1对于随机数组的复杂度为 O(nlogn)，但是对于相同元素的数组，复杂度接近 O(n^2)。
    # 这是因为，对于随机数组，每次的分界线m很可能是位于中间的，但是对于相同元素的数组，每次的分界线m都是第一个，因此logn退化成了n。
    n_list = list(range(2, 500))
    n2_list = list(map(lambda x:x*x, n_list))
    nlogn_list = list(map(lambda x:x*math.log2(x), n_list))
    count_list = []
    for n in n_list:
        #a = [0] * n # 相同元素的数组
        a = np.random.randint(0, 100, n) # 随机数组
        count = qsort1(a)
        count_list.append(count)
    plt.plot(n_list, count_list, 'r-', label='qsort1')
    plt.plot(n_list, n2_list, 'g-', label='n^2')
    plt.plot(n_list, nlogn_list, 'b-', label='nlogn')
    plt.legend()
    
        
        
                
                
        
    


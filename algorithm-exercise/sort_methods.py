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

def qsort2(a):
    '''
    加强版的快速排序，能够避免元素都相同时退化成O(n^2)的问题。
    1、随机选择一个值t，固定。
    2、初始化两个下标i和j，分别从左向右和从右向左扫描，不变式为a[0...i]<=t & a[j...]>=t，直到i和j相遇
    3、递归 qsort1([0...j-1]) 和 qsort1([j+1...])
    '''
    count = 0 # 记录迭代数
    def qsort2_rec(a, l, u):
        '''
        用于递归
        '''
        nonlocal count
        if l >= u:
            return
        
        # 初始化，将 t 定为第一个元素值
        t = a[l]
        i = l+1
        j = u
        
        # 遍历
        while(True):
            while(i <= u and a[i] < t): # i从左向右扫描，直到 a[i]>=t 停止
                i += 1
                count += 1
            while(j >= l+1 and a[j] > t): # j 从右向左扫描，直到 a[j]<=t 停止
                j -= 1
                count += 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i] # 交换值，则变成了 a[i]<=t，a[j]>=t
            i += 1 # 一定要有这一句，否则当 a[i]==a[j]==t时，会死循环
        # 最后一步，交换a[l]和a[j]的值
        a[j], a[l] = a[l], a[j]
        # 递归
        qsort2_rec(a, l, j-1)
        qsort2_rec(a, j+1, u)
    
    # 开始递归
    qsort2_rec(a, 0, len(a)-1)
    return count
    
    
if '__main__' == __name__:
    a = [32,1,456,234,7,23,87,123,456]
    qsort2(a)
    print(a)
    
    # 测试复杂度。
    # 结论：
    # 1、qsort1对于随机数组的复杂度为 O(nlogn)，但是对于相同元素的数组，复杂度接近 O(n^2)。这是因为，对于随机数组，每次的分界线m很可能是位于中间的，但是对于相同元素的数组，每次的分界线m都是第一个，因此logn退化成了n。
    # 2、qsort2对于随机数组和相同元素数组的复杂度均为 O(nlogn)，关键就在于i和j从两边搜索，且遇到等于t的时候也会停下来，因此如果是相同元素数组，就会一步一步进行交换，虽然交换次数很多且显得不必要，但是可以保证最后i与j相遇时是在数组的中间位置。
    n_list = list(range(2, 500))
    n2_list = list(map(lambda x:x*x, n_list))
    nlogn_list = list(map(lambda x:x*math.log2(x), n_list))
    sort_method_list = [qsort1, qsort2] # 所有排序函数
    figure_count = 0
    for sort_method in sort_method_list:
        count_list1 = [] # 相同元素的排序迭代次数
        count_list2 = [] # 随机元素的排序迭代次数
        for n in n_list:
            # 对相同元素数组进行排序
            a1 = [0] * n
            count_list1.append(sort_method(a1))
            # 对随机元素数组进行排序
            a2 = np.random.randint(0, 100, n)
            count_list2.append(sort_method(a2))
        
        # 画图
        figure_count += 1
        plt.figure(figure_count)
        plt.plot(n_list, n2_list, 'b-', label='n^2') # n^2的曲线
        plt.plot(n_list, nlogn_list, 'b-', label='nlogn') # nlogn的曲线
        plt.plot(n_list, count_list1, 'r-', label='same') # 相同元素复杂度曲线
        plt.plot(n_list, count_list2, 'g-', label='random') # 随机元素复杂度曲线
        plt.title(sort_method.__name__) # 函数名为title
        plt.legend()
    
        
        
                
                
        
    


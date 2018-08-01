# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 22:01:19 2018

@author: gongyanshang1

输入一个包含n个浮点数的数组，要求输出此数组的任何连续子数组中的最大和。
特殊地，如果数组中都是负数，则最大和为0，连续子数组长度为0。
"""

def find_max_sum_by_force(a):
    '''
    用暴力方法求解。复杂度为O(n^3)。
    '''
    max_sum = 0
    for i in range(0, len(a)):
        for j in range(i, len(a)):
            sum = 0
            for idx in range(i, j+1):
                sum += a[idx]
            if sum > max_sum:
                max_sum = sum
    return max_sum

def find_max_sum_by_force2(a):
    '''
    暴力求解。复杂度为O(n^2)。
    '''
    max_sum = 0
    for i in range(0, len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]
            if sum > max_sum:
                max_sum = sum
    return max_sum    

def find_max_sum_by_force3(a):
    '''
    暴力求解。复杂度为O(n^2)。
    '''
    
    # 先求出从第一个索引出发，到每个索引结束的子数组的和
    sum_list = [0] * (len(a) + 1) # 比a长一位是为了保证sum_list[-1]=0
    for i in range(0, len(a)):
        sum_list[i] = sum_list[i-1] + a[i]
    
    # 双重循环
    max_sum = 0
    for i in range(0, len(a)):
        for j in range(i, len(a)):
            sum = sum_list[j] - sum_list[i-1]
            if sum > max_sum:
                max_sum = sum
    return max_sum

def find_max_sum_by_recursion(a):
    '''
    递归求解。分治思想。复杂度为O(nlogn)
    '''
    
    # 定义递归结束标志
    if len(a) == 0:
        return 0
    if len(a) == 1:
        return max(a[0], 0)
    
    # 将数组分为两个数组，则原问题的最大和=max(前半部分的最大和，后半部分的最大和，包含中间数的子数组的最大和)
    midx = int(len(a) / 2)
    a1 = a[:midx]
    a2 = a[midx:]
    
    # 计算包含中间数的子数组的最大和
    # 计算左半部分的最大和
    lmax = 0
    sum = 0
    for i in range(midx-1, -1, -1):
        sum += a[i]
        if sum > lmax:
            lmax = sum
    # 计算右半部分的最大和
    rmax = 0
    sum = 0
    for i in range(midx, len(a)):
        sum += a[i]
        if sum > rmax:
            rmax = sum
    mid_max = lmax + rmax # 含中间数的子数组的最大和 = 左半部分的最大和 + 右半部分的最大和
    
    return max(find_max_sum_by_recursion(a1), find_max_sum_by_recursion(a2), mid_max)

def find_max_sum_by_dynamic(a):
    '''
    动态规划。复杂度为O(n)。思想是已知a[0:i]的最优解，如何求取a[0:i+1]的最优解。
    动态规划本质是将一个个子任务的结果存起来，供下一个子任务使用。空间换取时间。
    有点像数学归纳法，已经证明了前i-1步是正确的，然后根据第i-1步和第i步的关联关系，证明第i步也是正确的。
    '''
    max_sum = 0 # 存储当前子数组的最优解，供下一个子数组使用
    max_ending = 0 # 存储当前子数组的以最后一个元素结尾的子数组的最大和，供下一个子数组使用
    for i in range(0, len(a)): # 每个循环求解的是 a[0:i] 的最优解
        max_ending = max(0, max_ending + a[i]) # 末尾子数组的最大和，只有可能是三个值：0、末尾元素、上一个子数组的末尾子数组的最大和+末尾元素
        max_sum = max(max_sum, max_ending) # 当前子数组的最优解，只有可能是两个值：上一个子数组的最优解、当前末尾子数组的最大和
    return max_sum

def find_max_sum_by_scan(a):
    '''
    扫描方法，复杂度为O(n)。
    这个方法是从网上看到的，其实代码与动态规划是完全等价的。
    我把它单独又写了一个函数，是因为它使用了另一种思路来解释。
    算法思想：
    1、维护一个sum值，从第一个元素开始，依次往后累加
    2、比如已经累加了前i个元素，即 a[0]~a[i-1]。如果结果大于0则继续；
    3、如果小于0，则问题最优解只可能是两个值：a[i:]的最优解、a[:i-1]的最优解。a[i:]的最优解已经存储起来，因此将sum置0，重新开始累积，来计算 a[:i-1]的最优解。
      (这与find_max_sum_by_recursion方法来比，少了一个“包含中间数的子数组的最大和”。为什么不必考虑这个值？因为左半部分的最大和一定是0。很容易用反证法来证明此结论。)
    '''
    max_sum = 0
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]
        if sum < 0:
            sum = 0
        max_sum = max(max_sum, sum)
    return max_sum

def find_max_sum_by_scan2(a):
    '''
    递归方法，复杂度为O(n)。
    此方法受 find_max_sum_by_scan 方法启发。既然可以将最优解分解为 a[i:]的最优解、a[:i-1]的最优解 两部分，那么为什么不可以用递归呢？
    '''
    # 递归停止规则
    if len(a) == 0:
        return 0

    max_sum = 0
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]
        if sum < 0:
            return max(max_sum, find_max_sum_by_scan2(a[i+1:])) # return max(a[i:]的最优解, a[:i-1]的最优解)
        max_sum = max(max_sum, sum)
    return max_sum  

if '__main__' == __name__:
    a = [31,-41,59,26,-53,58,97,-93,-23,84]
    print(find_max_sum_by_force(a))
    print(find_max_sum_by_force2(a))
    print(find_max_sum_by_force3(a))
    print(find_max_sum_by_recursion(a))
    print(find_max_sum_by_dynamic(a))
    print(find_max_sum_by_scan(a))
    print(find_max_sum_by_scan2(a))


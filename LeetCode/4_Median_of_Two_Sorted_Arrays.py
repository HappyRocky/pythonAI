# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 09:22:06 2018

@author: gongyanshang1

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

有两个已经排好序（升序）的数组 nums1 和 nums2，大小分别为 m 和 n。
要求找到两个数组的中位数。时间复杂度需要为 O(log(m+n))。
两个数组不会同时为空。

示例：
Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5

"""

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    
    思路：
    两个数组都是有序的，让我想起了归并排序：将两个有序数组合在一起并排序，只需要用两个指针分别扫描两个数组，每次指针+1并比较大小。
    这道题可以直接使用归并排序，然后找到中位数，但是这样复杂度为O(m+n)，不满足条件。
    由于这道题只需要找到中位数，其他元素是否排序无关紧要，因此，两个指针不必每次只+1，而是每次加一个最合适的值，使得整体复杂度最小。
    """
    
    def fun_rec(nums1, i, nums2, j, k):
        '''
        找到两个数组的整体排序后的第 i+j+k 个数。分别已经扫描过了前i个和前j个，需要在此基础上找到第 k 个数。
        '''
        
        # 递归结束条件
        if i == len(nums1):
            return nums2[j+k-1]
        if j == len(nums2):
            return nums1[i+k-1]
        if k == 1:
            return min(nums1[i], nums2[j])
        
        # 保证前一个数组的剩余长度比后一个数组要短，这样只要控制好前一个数组的下标，就不用判断后一个数组是否会溢出
        if len(nums1) - i > len(nums2) - j:
            return fun_rec(nums2, j, nums1, i, k)
        
        # 两个指针分别从i和j开始，都直接加上 k/2，然后比较大小，选出较小的那个数组，继续和另一个数组进行递归。
        ii = i + int(k/2)
        ii = min(ii, len(nums1)) # 不能溢出
        jj = i+j+k-ii # 保证 (ii-i)+(jj-j) == k，即 ii和jj的增量的和正好是k，这样可以达到每次尽可能增加最大的下标增量，而又不会越过第k个数
        if nums1[ii-1] == nums2[jj-1]: # 相等，说明正好是第k个数
            return nums1[ii-1]
        if nums1[ii-1] < nums2[jj-1]: # 前一个值小，说明在最终第k个数，肯定在ii之后
            return fun_rec(nums1, ii, nums2, j, k+i-ii) # 始终保持 fun_rec 函数的第2、4、5的参数的和等于 i+j+k
        return fun_rec(nums1, i, nums2, jj, k+j-jj)
    
    # 判断应该寻找第几个数
    total = len(nums1) + len(nums2)
    if total % 2 == 1: # 奇数，需要寻找最中间的那个数
        return fun_rec(nums1, 0, nums2, 0, int((total+1)/2))
    else: # 偶数，需要求中间两个数的均值
        return (fun_rec(nums1, 0, nums2, 0, int(total/2)) + fun_rec(nums1, 0, nums2, 0, int(total/2+1))) / 2
    
def findMedianSortedArrays2(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    
    上一个方法有个缺点，就是如果是偶数，那么在求中间两个数的时候，大部分过程是重复的。
    改进：将fun_rec输出第k个数改为输出第k个数和第k+1个数。
    
    """
    
    def fun_rec(nums1, i, nums2, j, k):
        '''
        找到两个数组的整体排序后的第 i+j+k 个数和右邻的数。分别已经扫描过了前i个和前j个，需要在此基础上找到第 k 个数。
        '''
        
        # 递归结束条件
        if i == len(nums1):
            return (nums2[j+k-1], nums2[j+k])
        if j == len(nums2):
            return (nums1[i+k-1], nums1[i+k])
        if k == 1:
            if nums1[i] < nums2[j]:
                return (nums1[i], find_next(nums1, i, nums2, j-1))
            else:
                return (nums2[j], find_next(nums2, j, nums1, i-1))
        
        # 保证前一个数组的剩余长度比后一个数组要短，这样只要控制好前一个数组的下标，就不用判断后一个数组是否会溢出
        if len(nums1) - i > len(nums2) - j:
            return fun_rec(nums2, j, nums1, i, k)
        
        # 两个指针分别从i和j开始，都直接加上 k/2，然后比较大小，选出较小的那个数组，继续和另一个数组进行递归。
        ii = i + int(k/2)
        ii = min(ii, len(nums1)) # 不能溢出
        jj = i+j+k-ii # 保证 (ii-i)+(jj-j) == k，即 ii和jj的增量的和正好是k，这样可以达到每次尽可能增加最大的下标增量，而又不会越过第k个数
        if nums1[ii-1] == nums2[jj-1]: # 相等，说明正好是第k个数
            return (nums1[ii-1], find_next(nums1, ii-1, nums2, jj-1))
        if nums1[ii-1] < nums2[jj-1]: # 前一个值小，说明在最终第k个数，肯定在ii之后
            return fun_rec(nums1, ii, nums2, j, k+i-ii) # 始终保持 fun_rec 函数的第2、4、5的参数的和等于 i+j+k
        return fun_rec(nums1, i, nums2, jj, k+j-jj)
    
    def find_next(nums1, i, nums2, j):
        '''
        nums1已经扫描到了i，nums2已经扫描到了j。
        返回 nums1[i] 的下一个大的元素。
        '''
        if i == len(nums1) - 1:
            return nums2[j+1]
        return min(nums1[i+1], nums2[j+1])
    
    # 判断应该寻找第几个数
    if len(nums1)== 0 and len(nums2) == 1:
        return nums2[0]
    if len(nums2)== 0 and len(nums1) == 1:
        return nums1[0]    
    total = len(nums1) + len(nums2)
    result = fun_rec(nums1, 0, nums2, 0, int((total+1)/2))
    if total % 2 == 1: # 奇数，需要寻找最中间的那个数
        return result[0]
    else: # 偶数，需要求中间两个数的均值
        return (result[0]+result[1])/2
    
if '__main__' == __name__:
    nums1 = [1, 3]
    nums2 = [2]
    print(findMedianSortedArrays2(nums1, nums2))
    
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(findMedianSortedArrays2(nums1, nums2))
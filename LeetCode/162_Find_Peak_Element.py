# -*- coding: utf-8 -*-

"""
A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.
Your solution should be in logarithmic complexity.

一个峰值指的是比它的邻居都要高的元素。
给定一个数组 nums，其中 nums[i] ≠ nums[i+1]，找到一个峰值并返回它的索引。
数组可能会包含多个峰值，则返回任意一个即可。
可以假设 nums[-1] = nums[n] = -∞。
算法的时间复杂度需要是对数复杂度。

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
"""

def findPeakElement(nums: list) -> int:
    """
    由于两端可以认为是无穷小，因此可以用二分法来求解。
    """
    if not nums:
        return None
    nums = [float('-inf')] + nums + [float('-inf')]
    
    def binarysearch(i, j):
        """
        二分法查找nums中的峰值
        """
        # 递归结束
        if j - i == 2:
            return i + 1
        # 二分
        mid = (i + j) // 2
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]: # 符合条件
            return mid
         # 搜寻较高的那一部分
        if nums[mid] < nums[mid+1]:
            return binarysearch(mid, j)
        return binarysearch(i, mid)
        
    return binarysearch(0, len(nums) - 1) - 1

if '__main__' == __name__:
    nums = [1,2,1,3,5,6,4]
    print(findPeakElement(nums))
# -*- coding: utf-8 -*-

'''
Given an unsorted integer array, find the smallest missing positive integer.

给定一个乱序的整数数组，找到最小的缺失的正整数。

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1
'''

def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    如果 nums 的长度为 l，则结果肯定是在 1 ~ (l+1) 中的某个数，
    因为当 nums 包含了 1~l 的所有值时， 算法结果最大，为 l+1。
    因此只需要定义一个额外的数组 list2，长度为 l，元素都为 0。
    遍历 nums，每遇到一个小于等于 l 的元素值 a，便将 list2 中的a索引标记为1。
    之后再遍历一遍 list2， 找到第一个为 0 的位置，这个位置即为最小的缺失正整数。
    """
    
    l = len(nums)
    if l == 0:
        return 1
    
    list2 = [0] * l
    for i in nums:
        if i > 0 and i <= l:
            list2[i-1] = 1
    
    for i in range(l):
        if list2[i] == 0:
            return i+1
    return l+1

def firstMissingPositive2(nums):
    """
    :type nums: List[int]
    :rtype: int
    改进版。
    不再额外创建一个新数组，而是将 nums 当做新数组。
    注意，由于 nums 之前便有数据，因此在修改 nums 值时，需要将原来的值保存下来，即与当前指针的值互换位置。
    """
    
    l = len(nums)
    if l == 0:
        return 1
    
    for i in range(l):
        while nums[i] > 0 and nums[i] <= l and nums[nums[i]-1] != nums[i]:
            j = nums[nums[i]-1]
            nums[nums[i]-1] = nums[i]
            nums[i] = j
    
    for i in range(l):
        if nums[i] != i+1:
            return i+1
    return l+1

if '__main__' == __name__:
    nums = [3,4,-1,1]
    print(firstMissingPositive2(nums))
        
    
    
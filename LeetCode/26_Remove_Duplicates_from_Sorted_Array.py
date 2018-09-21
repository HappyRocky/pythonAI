# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 09:36:12 2018

@author: gongyanshang1

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

给定一个有序数组，去除重复的元素，返回新的数组长度。
备注：
如果返回的新数组长度为m，则需要保证数组的前m个元素一定包含了所有的去重后的元素，之后的元素值不作要求。
不要为另外的数组去开辟新的空间，只能修改原数组，空间复杂度为O(1)。

示例：
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

"""

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    从左到右扫描，维护一个变量，始终等于前一个元素。这样就可以知道当前元素是否是重复元素。
    如果重复了，删除这个元素。
    此方法会改变原数组的长度。
    """
    if len(nums) <= 1:
        return len(nums)
    
    idx = 1
    while(idx < len(nums)):
        if nums[idx] == nums[idx - 1]:
            del nums[idx]
        else:
            idx += 1
    return idx

def removeDuplicates2(nums):
    """
    :type nums: List[int]
    :rtype: int
    从左到右扫描，维护一个索引，这个索引始终保持为去重后元素的最后一位。
    如果扫描到了一个元素和这个索引的元素不同，则将索引+1，且索引对应的值修改为当前元素值。
    此方法不会改变数组的长度。
    """
    if len(nums) <= 1:
        return len(nums)
    
    idx = 0
    for num in nums:
        if num != nums[idx]:
            idx += 1
            nums[idx] = num
    return idx + 1

if '__main__' == __name__:
    nums = [1,1,2]
    print(removeDuplicates2(nums))
    
# -*- coding: utf-8 -*-

'''
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

给定一个升序数组和一个目标值，返回目标值的索引。
如果不存在，返回目标值按照顺序应该插入到的位置。
假设数组中没有重复元素。

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0

'''

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    二分法查找。
    结束条件需要改变一下：当查找到最后两位时，如果都不满足，则返回应该插入到的位置。
    """
    def binary_search(nums, l, u, target):
        '''
        二分法查找。
        调用此函数之前需要保证：
        1、nums[l] <= target <= nums[u]
        2、len(nums) >= 2
        '''
        if u - l == 1:
            if nums[l] == target:
                return l
            else:
                return u
        
        mid = (l+u) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return binary_search(nums, mid, u, target)
        else:
            return binary_search(nums, l, mid, target)
        
    if not nums:
        return 0
    if target <= nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums)
    return binary_search(nums, 0, len(nums)-1, target)
    
if '__main__' == __name__:
    nums, target = [1,3,5,6], 0
    print(searchInsert(nums, target))
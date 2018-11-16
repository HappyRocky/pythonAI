# -*- coding: utf-8 -*-
'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

给定一个升序整数数组，找到一个目标值的起始和结束位置。
算法的时间复杂度必须为 O(log n)
如果目标值不存在，则返回 [-1,-1]

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    二分法。
    在查找到target之后，继续使用二分法，查找起始和结束位置。
    """
    
    def binary_search(nums, l, u, target, max_len):
        '''
        二分法查找nums的l~u之间等于target的元素，返回起始和结束位置。
        如果不存在，则返回 (max_len, -1)
        '''
        # 递归结束条件1
        if u - l <= 1: # 数组长度小于等于2
            # 初始化首尾位置
            start = max_len
            end = -1
            # 依次与目标值进行比较
            for i in range(l, u+1):
                if nums[i] == target:
                    start = min(start, i)
                    end = max(end, i)
            return (start, end)
        
        # 递归结束条件2
        if nums[l] == nums[u]: # 数组首尾元素相等，则中间元素也都相等
            if nums[l] == target:
                return (l, u)
            else:
                return (max_len, -1)
        
        # 开始二分法
        mid = int((l+u)/2)
        if nums[mid] == target: # 中位数等于目标值
            # 寻找左半部分的首尾位置
            start1, end1 = binary_search(nums, l, mid, target, max_len)
            # 寻找右半部分的首尾位置
            start2, end2 = binary_search(nums, mid, u, target, max_len)
            # 两个首尾位置比较大小
            start = min(start1, start2)
            end = max(end1, end2)
            return (start, end)
        elif nums[mid] > target: # 目标值小于中位数
            # 寻找左半部分的首尾位置
            return binary_search(nums, l, mid, target, max_len)
        else:
            # 否则，寻找右半部分的首尾位置
            return binary_search(nums, mid, u, target, max_len)
    
    if not nums or target < nums[0] or target > nums[-1]:
        return [-1, -1]
    max_len = len(nums)
    start, end = binary_search(nums, 0, max_len-1, target, max_len)
    if start == max_len:
        start = -1
    return [start, end]

if '__main__' == __name__:
    nums = [5,6,7,8,8,10]
    target = 10
    print(searchRange(nums, target))
    
    
    

# -*- coding: utf-8 -*-

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

给定一个数组，这个数组是由一个升序数组进行左旋或右旋若干次得到的。
比如，[0,1,2,4,5,6,7] 可能会变为 [4,5,6,7,0,1,2]
给定一个目标值，去数组中查询这个值。如果找到，则返回索引，否则返回-1。
可以假设数组中没有重复值。
算法复的时间复杂度必须为 O(logn)

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

'''

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    二分法。
    由于是有序数组旋转得到的，所以与一般二分法有区别。
    """
    
    if not nums:
        return -1
    
    l, u = 0, len(nums)-1
    while(l <= u):
        # 长度为1或2
        if u - l <= 1:
            try:
                return l + nums[l:u+1].index(target)
            except:
                return -1
        
        mid = int((l + u) / 2)
        if nums[mid] == target:
            return mid
        
        if nums[mid] > nums[l]: # 说明mid落在了左半部分
            if target > nums[mid]:
                l = mid + 1
            elif target >= nums[l]:
                u =  mid-1
            else:
                l = mid + 1
        else:
            if target < nums[mid]:
                u = mid - 1
            elif target <= nums[u]:
                l = mid + 1
            else:
                u = mid - 1
        
if '__main__' == __name__:
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(search(nums, target))
                
                  
            
        
        
    
    
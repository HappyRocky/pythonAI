# -*- coding: utf-8 -*-

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.

假设一个升序数组已经被旋转了若干次。
比如 [0,0,1,2,2,5,6] 可能会旋转成 [2,5,6,0,0,1,2]
给定一个待寻找的目标值，如果数组中有这个值则返回true，否则返回false。

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

'''

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    这与第81题很相近，区别是本题数组中可能有重复值。
    还是使用二分法，但是由于可能有重复值，所以在遇到mid和l相等时不能判断mid和l之间是否是递增的，因而不能确定下一次递归应该选择左半区间还是右半区间，这时候需要两个区间都尝试。
    """
    
    def binary_search(nums, u, l, target):
        '''
        二分法查找target
        '''
        # 递归结束条件
        if u - l <= 1:
            return target in nums[l:u+1]

        # 中位数        
        mid = int((l + u) / 2)
        if nums[mid] == target:
            return True
        
        if nums[mid] > nums[l]: # 说明 l 与 mid 之间是递增的
            if target <= nums[mid] and target >= nums[l]:
                u = mid - 1
            else:
                l = mid + 1
            return binary_search(nums, u, l, target)
        elif nums[mid] < nums[l]: # 说明 l 位于左半部分，mid 与 u 位于右半部分， mid 与 u 之间是递增的
            if target >= nums[mid] and target <= nums[u]:
                l = mid + 1
            else:
                u = mid - 1
            return binary_search(nums, u, l, target)
        else: # 相等，不知道l,mid,u位于哪半部分，因此两个区间都尝试查找
            return binary_search(nums, u, mid+1, target) or binary_search(nums, mid-1, l, target)
    return binary_search(nums, len(nums)-1, 0, target)
                
if '__main__' == __name__:
    nums = [1,3,1,1,1]
    target = 3
    print(search(nums, target))
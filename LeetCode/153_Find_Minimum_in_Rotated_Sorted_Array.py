# -*- coding: utf-8 -*-

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.

假设有一个升序数组，且已经被旋转了若干次。
比如，[0,1,2,4,5,6,7] 可能会被旋转为 [4,5,6,7,0,1,2]。
找到最小元素。
可以假设数组中没有重复元素。

Example 1:
Input: [3,4,5,1,2] 
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
"""

def findMin(nums: list) -> int:
    """
    二分法。
    根据起始、末尾和中间三个位置的数的大小关系，来判断最小值存在前半部分还是后半部分。
    """
    # 递归结束条件
    if len(nums) <= 3:
        return min(nums)
    # 分为两部分
    mid = int(len(nums) / 2)
    if nums[0] < nums[-1]: # 整个nums肯定是升序
        return nums[0]
    if nums[mid] > nums[0]:
        return findMin(nums[mid+1:])
    return findMin(nums[:mid+1])

if '__main__' == __name__:
    nums = [4,5,6,7,0,1,2]
    print(findMin(nums))
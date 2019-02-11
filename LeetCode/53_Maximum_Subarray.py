# -*- coding: utf-8 -*-

'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

给定一个整数数组，找到连续子数组（至少包含一位）的最大和，并返回。

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    分治法。
    nums 的连续子数组的最大和，就等于以下三者中的最大值：
    1、nums[:mid] 的连续子数组的最大和
    2、nums[mid+1:] 的连续子数组的最大和
    3、包含nums[mid] 的连续子数组的最大和
    其中，mid 为中位数位置。
    时间复杂度的递推公式：T(n) = 2*T(n/2) + n
    可求出：T(n) = O(nlogn)
    """
    
    # 递归结束条件
    l = len(nums)
    if l == 1:
        return nums[0]
    
    # 求取包含nums[mid] 的连续子数组的最大和
    mid = l // 2
    max_sum1 = 0 # mid 左半部分的最大和（从末尾向前累加）
    cur_sum = 0
    for num in nums[:mid][::-1]:
        cur_sum += num
        max_sum1 = max(max_sum1, cur_sum)
    max_sum2 = 0 # mid 右半部分的最大和（从起始向后累加）
    cur_sum = 0
    for num in nums[mid+1:]:
        cur_sum += num
        max_sum2 = max(max_sum2, cur_sum)
    max_sum = nums[mid] + max_sum1 + max_sum2
    
    # 返回三者的最大值
    return max(max_sum, maxSubArray(nums[:mid]), maxSubArray(nums[mid+1:]))

def maxSubArray2(nums):
    """
    :type nums: List[int]
    :rtype: int
    动态规划法
    已知前 k 项的最大子数组之和，求前 k+1 项的最大子数组之和，就等于以下两者的较大值：
    1、前 k 项的最大子数组之和
    2、包含 nums[k] 的最大子数组之和
    其中第2步，包含 nums[k] 的最大子数组之和，又可以根据前 k 项中包含 nums[k-1] 的最大子数组之和来得到，只需要O(1)。
    因此整体时间复杂度为 O(n)。
    """
    sub_max = nums[0] # 存储前i项的最大子数组之和
    last_max = nums[0] # 存储前i项的且包含最后一位的最大子数组之和
    
    for i in range(1, len(nums)):
        last_max = max(last_max + nums[i], nums[i])
        sub_max = max(sub_max, last_max)
        
    return sub_max

if '__main__' == __name__:
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray2(nums))
    
    
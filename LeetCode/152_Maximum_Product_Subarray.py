# -*- coding: utf-8 -*-

"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

给定一个整数数组，找到连续子数组（至少包含一个数字）的最大乘积。

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

def maxProduct(nums: list) -> int:
    """
    线性规划
    """
    imax = imin = nums[0]
    result = nums[0]
    for num in nums[1:]:
        if num < 0:
            imax, imin = imin, imax
        imax = max(imax*num, num)
        imin = min(imin*num, num)
        result = max(result, imax)
    return result

if '__main__' == __name__:
    nums = [2,3,-2,4]
    print(maxProduct(nums))
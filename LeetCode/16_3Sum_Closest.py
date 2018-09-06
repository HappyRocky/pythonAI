# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 09:32:22 2018

@author: gongyanshang1

Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

给定一个数组，包含n个整数，以及一个目标整数。
要求在数组中找到三个数，使得这三个数之和最接近目标整数。
返回三数之和。
假设每个输入都只有一个答案。

示例:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""
def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    与第15题思想类似，也是外层循环+首尾指针，只不过本题需要记录每一次与target的差值，并将最小差值存储下来。
    
    """
    
    if len(nums) < 3:
        return []
    
    nums.sort()
    min_diff = sum(nums[:3]) - target
    for i in range(len(nums) - 2):
        if i > 0 and nums[i-1] == nums[i]: # 避免i重复
            continue
        l, r = i + 1, len(nums) - 1 
        while l < r:
            diff = nums[i] + nums[l] + nums[r] - target
            if diff == 0: # 正好等于target，直接返回，肯定是最小差值
                return target
            else:
                if abs(diff) < abs(min_diff): # 更新最小差值
                    min_diff = diff
                # 根据diff大小判断哪个指针需要移动
                if diff < 0: # 三数之和不够则往右走
                    l += 1
                else: # 三数之和过大则往左走
                    r -= 1
    return min_diff + target

if '__main__' == __name__:
    nums = [-1, 0, 1, 1, 55]
    target = 3
    print(threeSumClosest(nums, target))
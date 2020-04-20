# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 15:09:48 2018

@author: gongyanshang1

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

给定一个整数的数组，返回两个元素的下标，这两个元素相加等于一个给定值。
可以假设每一个输入都只有一种答案。

示例：
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    match_idx_dict = dict()  # key=差值,value=下标
    for i in range(len(nums)):
        num = nums[i]
        if num not in match_idx_dict:
            match_idx_dict[target - num] = i
        else:
            return [match_idx_dict[num], i]
    return None


if '__main__' == __name__:
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))

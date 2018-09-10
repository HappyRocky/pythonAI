# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 09:11:47 2018

@author: gongyanshang1

Given an array nums of n integers and an integer target, 
are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

给定一个长度为n的整数数组，一个目标整数target。
在数组中找到4个数a,b,c,d，使得 a+b+c+d=target。
要求找到所有不重复的四元组合。

示例:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""

def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    在3Sum的基础（https://github.com/HappyRocky/pythonAI/blob/master/LeetCode/15_3Sum.py）上，多一层循环。
    """
    if len(nums) < 4:
        return []
    
    nums.sort()
    res = []
    
    for o in range(len(nums) - 3):
        if o > 0 and nums[o-1] == nums[o]: # 避免o重复
            continue
        for i in range(o + 1, len(nums) - 2):
            if i > o+1 and nums[i-1] == nums[i]: # 避免i重复
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[o] + nums[i] + nums[l] + nums[r]
                if s == target:
                    res.append([nums[o], nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: # 避免l重复
                        l += 1
                    while l < r and nums[r] == nums[r+1]: # 避免r重复
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
    return res

def fourSum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    上述方法的改良版。
    改良的关键主要体现在循环之前先通过最小几个数相加和最大几个数相加判断是否有继续嵌套循环的必要。
    使用递归是为了防止代码重复，否则第一层和第二层循环都要加上提前判断的代码。
    使用递归的另一个好处是，可以不仅仅是4个数相加，任意大于等于3的数相加，都可以用这套代码。
    """
    
    def findComb(nums, size, target, ans, start, ansSize, tempAns):
        '''
        递归函数。从nums的start下标开始往后，找到ansSize个整数，使得相加等于target。
        size为nums的大小，固定不变。
        ans存放最终答案。
        tempAns存放当前4元组内已经找到的元素，len(tmpAns)总是等于4-ansSize。
        '''
        if sum(nums[start:start+ansSize]) > target: # 最小的几个数相加都超出
            return
        if sum(nums[-ansSize:]) < target: # 最大的几个数相加都不够
            return
        if ansSize == 2: # 需要寻找2个，则使用首尾指针法。
            i = start
            j = size - 1
            while(i < j):
                sigma = nums[i] + nums[j]
                if sigma > target:
                    j -= 1
                elif sigma < target:
                    i += 1
                else:
                    ans.append(tempAns + [nums[i], nums[j]])
                    j -= 1
                    while(i < j and nums[j] == nums[j + 1]): # skip repeats
                        j -= 1
                    i += 1
                    while(i < j and nums[i] == nums[i - 1]): # skip repeats
                        i += 1
        else:
            for i in range(start, size - ansSize + 1):
                if i > start and nums[i] == nums[i - 1]: # skip repeats
                    continue
                findComb(nums, size, target - nums[i], ans, i + 1, ansSize - 1, tempAns + [nums[i]])
    
    ans = []
    size = len(nums)
    
    if size < 4:
        return []
    if size == 4:
        if sum(nums) == target:
            return [nums]
        else:
            return []

    nums.sort()

    findComb(nums, size, target, ans, 0, 4, [])
    return ans


if '__main__' == __name__:
    nums = [0, 0, 0, 0]
    target = 0
    print(fourSum2(nums, target))
            
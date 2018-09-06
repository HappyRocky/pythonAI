# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 09:33:25 2018

@author: gongyanshang1

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.

给定一个整数数组，长度为n，要求判断出是否存在3个元素a,b,c使得a+b+c=0？
找到所有不重复的三元组。

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

def threeSum(nums):
    '''
    先排序，再开始查找，查找时定义两个指针，一头一尾，向中间合拢。排序后可以方便判定哪个指针需要移动。
    '''
    if len(nums) < 3:
        return []
    
    nums.sort()
    res = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i-1] == nums[i]: # 避免i重复
            continue
        l, r = i + 1, len(nums) - 1 
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]: # 避免l重复
                    l += 1
                while l < r and nums[r] == nums[r+1]: # 避免r重复
                    r -= 1
            elif s < 0: # 因此三数之和不够则往右走
                l += 1
            else: # 因此三数之和过大则往左走
                r -= 1
    return res

if '__main__' == __name__:
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))
            
            
            
    
    


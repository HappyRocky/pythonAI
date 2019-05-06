# -*- coding: utf-8 -*-

"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

给定一个整数序列，可能会包括重复数字，返回所有可能的子集。
备注：不能包含重复的子集。

Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2], 
  []
]
"""

def subsetsWithDup(nums: list) -> list:
    """
    递归。
    nums 的所有子集 = nums[:i] 的所有子集 * nums[i:] 的所有子集，任取i都可以，只要 nums[:i] 与 nums[i:] 之间没有相同的元素
    """
    def get_sub(nums):
        """
        递归求取nums的子集，前提是 nums 是有序的。
        """
        # 递归结束条件
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [[], nums]
        if nums[0] == nums[-1]: # nums中所有元素均相同
            return [[nums[0]] * i for i in range(len(nums) + 1)]
        # 寻找前i个相同元素
        for i in range(len(nums)):
            if nums[i] != nums[0]:
                break
        # 以i为界分为两部分，分别求出两部分的子集，然后进行笛卡尔积
        result1 = get_sub(nums[:i])
        result2 = get_sub(nums[i:])
        result = []
        for sub1 in result1:
            for sub2 in result2:
                result.append(sub1 + sub2)
        return result
    
    nums1 = sorted(nums)
    return get_sub(nums1)

def subsetsWithDup2(nums):
    """
    每次扫描到一个元素，就把这个元素加到已有结果集的每个列表的最后。
    """
    if not nums:
        return []
    nums.sort()
    res, cur = [[]], [] # res为结果集， cur为包含当前元素的结果集
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]: # nums[i] 为新出现的一个元素，则在结果集的每一个列表后都加上这个新元素
            cur = [item + [nums[i]] for item in res]
        else: # nums[i] 为重复元素，则只在上一次 cur 的每一个列表后加上这个元素，不必在所有结果集的列表后都加上这个元素，防止重复
            cur = [item + [nums[i]] for item in cur] 
        res += cur
    return res

if '__main__'  == __name__:
    nums = [1,2,2]
    print(subsetsWithDup2(nums))

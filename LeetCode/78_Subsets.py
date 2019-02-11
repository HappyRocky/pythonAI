# -*- coding: utf-8 -*-

'''
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

给定一个无重复的整数列表 nums，返回所有可能的子集（幂集）。
备注：返回结果中不能有重复的子集。

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    幂集（Power Set）， 就是原集合中所有的子集（包括全集和空集）构成的集族。
    幂集的大小为 2^n。
    可以使用递归法，从第一个开始遍历，有两种方式：选择这一个和不选择这一个。
    然后递归从剩下的数字中选择。
    """
    def select(result_list, pre_list, remain_list):
        '''
        从列表remain_list中获取所有子集，与pre_list拼接到一起，追加到结果列表中
        '''
        # 递归结束条件
        if not remain_list:
            result_list.append(pre_list)
            return
        # 选择第一个数，然后递归处理剩余的数
        select(result_list, pre_list+[remain_list[0]], remain_list[1:])
        # 略过第一个数，然后递归处理剩余的数
        select(result_list, pre_list, remain_list[1:])
    result_list = []
    select(result_list, [], nums)
    return result_list

if '__main__' == __name__:
    nums = [1,2,3]
    print(subsets(nums))
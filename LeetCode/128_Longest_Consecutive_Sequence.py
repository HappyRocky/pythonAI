# -*- coding: utf-8 -*-

"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.

给定一个乱序的整数序列，找到连续元素序列的最长长度。
算法的时间复杂度需要为 O(n)

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

def longestConsecutive(nums: list) -> int:
    """
    维护一个字典，存放包含每个元素的连续序列的最长长度。
    """
    len_dict = dict() # <num, length>存放包含每个元素的连续序列的最长长度
    max_len = 0
    for num in nums:
        if num in len_dict:
            continue
        left_len = len_dict.get(num - 1, 0) # 包含num-1的最长连续序列长度（里面肯定不会包含num，否则本次扫描num会被continue）
        right_len = len_dict.get(num + 1, 0)# 包含num+1的最长连续序列长度
        cur_len = left_len + right_len + 1 # 包含num的最长连续序列长度
        len_dict[num] = cur_len
        max_len = max(max_len, cur_len)
        # 更新两端的最长值
        len_dict[num - left_len] = cur_len
        len_dict[num + right_len] = cur_len
    return max_len

if '__main__' == __name__:
    nums = [1,2,0,1]
    print(longestConsecutive(nums))
    
            
        
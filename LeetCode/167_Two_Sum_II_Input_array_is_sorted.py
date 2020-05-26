# -*- coding: utf-8 -*-

"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

给定一个升序数组，找到两个数字，他们相加等于目标值。
函数需要返回两个数字的索引，index1必须小于index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

备注：
返回的下标值不是从0开始的
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


class Solution:
    def twoSum(self, numbers, target):
        if len(numbers) <= 1:
            return []
        sum_dict = dict()
        for i in range(len(numbers)):
            if numbers[i] in sum_dict:
                return [sum_dict[numbers[i]] + 1, i + 1]
            sum_dict[target - numbers[i]] = i
        return []


if '__main__' == __name__:
    solution = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(numbers, target))

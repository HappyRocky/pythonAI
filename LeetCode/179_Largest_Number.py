# -*- coding: utf-8 -*-
"""
Given a list of non negative integers, arrange them such that they form the largest number.

给定一个非负整数列表，将它们排序，让他们能够组成最大的数字。

Example 1:
Input: [10,2]
Output: "210"

Example 2:
Input: [3,30,34,5,9]
Output: "9534330"
"""
from functools import cmp_to_key

class Solution:
    def cmp(self, n1, n2):
        if n1 == n2:
            return 0
        # 确保n1是较短的字符串
        n1, n2 = str(n1), str(n2)
        transfor = 1
        if len(n1) > len(n2):
            n2, n1 = n1, n2
            transfor = -1
        # 从第一位开始比较
        i = len(n1)
        if int(n1) > int(n2[:i]):
            return transfor
        if int(n1) < int(n2[:i]):
            return 0 - transfor
        # n1是n2的子串，则继续n2剩余字符和n1的大小
        return transfor * self.cmp(n1, n2[i:])

    def largestNumber(self, nums) -> str:
        nums.sort(key=cmp_to_key(self.cmp), reverse=True)
        a = [str(x) for x in nums]
        return str(int(''.join(a)))  # 转int再转str的原因是将 '00' 转为 '0'


if '__main__' == __name__:
    nums = [3,30,34,5,9]
    print(Solution().largestNumber(nums))
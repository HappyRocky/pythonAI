# -*- coding: utf-8 -*-

"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

给定一个字符串 s，将 s 进行划分，每个子串都是一个回文子串。
返回所有可能的 s 的回文划分。

Example:
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

def partition(s: str) -> list:
    """
    递归，先提取出前缀子串，再继续处理剩下的。
    """
    result = []
    for i in range(1, len(s) + 1):
        if s[:i] == s[i-1::-1]:
            for part in partition(s[i:]):
                result.append([s[:i]] + part)
    if not result:
        return [[]]
    return result

def partition2(s: str) -> list:
    """
    将方法一改写为一行
    """
    return [[s[:i]] + part
            for i in range(1, len(s) + 1)
            if s[:i] == s[i-1::-1]
            for part in partition(s[i:])
            ] or [[]]

if '__main__' == __name__:
    s = "aab"
    print(partition2(s))
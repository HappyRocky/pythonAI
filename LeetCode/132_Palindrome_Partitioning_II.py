# -*- coding: utf-8 -*-

"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

给定一个字符串 s，将 s 进行划分，每个子串都是一个回文子串。
返回所有对 s 的回文划分中最小划分次数。

Example:
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

def minCut(s: str) -> int:
    """
    动态规划。
    记cut[i]为s[0...i]的最小划分次数，则
    cut[i] = min(cut[j-1]+1)，其中j<=i，且s[j...i]是一个回文子串。
    判断s[j...i]是否是一个回文子串时有一个便捷方法：判断是否满足 s[j] == s[i] 且 s[j+1,...,i-1]是一个回文子串。
    """
    n = len(s)
    palin_set = set() # 存放回文子串的始末位置
    cut = [0] * n # 存放前缀子串的最小划分次数
    for i in range(n):
        min_cut = i # 初始化为最大值，最大划分就是把每个字符都互相划分开来
        for j in range(i+1):
            # 判断 s[j...i] 是否是回文子串
            if s[j] == s[i] and (j+1 >= i-1 or (j+1, i-1) in palin_set):
                palin_set.add((j, i))
                min_cut = min(min_cut, cut[j-1] + 1) if j > 0 else 0
        cut[i] = min_cut
    return cut[n-1]

if '__main__' == __name__:
    s = "aab"
    print(minCut(s))
    
    
# -*- coding: utf-8 -*-

"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

给定一个非空字符串 s 和一个非空单词数组 wordDict。判断 s 是否可以被切割为数组中的一个或多个单词。
备注：
字典中同一个单词可能会使用多次。
可以假设字典中不包含重复单词。

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
             
Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

def wordBreak(s: str, wordDict: list) -> bool:
    """
    深度优先划分。
    """
    # 递归结束
    if not s:
        return True
    # 深度优先
    for w in wordDict:
        if w == s[:len(w)] and wordBreak(s[len(w):], wordDict):
                return True
    return False

def wordBreak2(s: str, wordDict: list) -> bool:
    """
    动态规划。
    维护一个数组dp，记 dp[i] 表示 s 的长度为 i 的前缀子字符串是否可切割。
    则递推关系式为：
    dp[j] = [ True, if 存在 i<j，使得 dp[i]==True 且 s[i:j] 等于 wordDict 的某个词。
            [ False
    """
    dp = [True] + [False] * len(s)
    for j in range(1, len(dp)):
        for i in range(j):
            if dp[i] and s[i:j] in wordDict:
                dp[j] = True
    return dp[-1]
    

if '__main__' == __name__:
    s =  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(wordBreak2(s, wordDict))
    
    
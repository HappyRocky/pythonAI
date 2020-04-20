# -*- coding: utf-8 -*-

"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

给定字符串 S 和 T，计算 S 的子序列中等于 T 的个数。
子序列指的是一个新的字符串，由原字符串构成，但是删除了一些（或者没有删除）字符，且没有打乱字符之间的相对顺序。
比如，"ACE" 是 "ABCDE" 的一个子序列，但是 "AEC" 不是。

Example 1:
Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

Example 2:
Input: S = "babgbag", T = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""

def numDistinct(s: str, t: str) -> int:
    """
    回溯法
    """
    def fun(s:str, t:str, count):
        """
        s的子序列等于t的个数，赋给count[0]
        """
        if not t:
            count[0] += 1
            return
        # 在s中查找等于t首字符的位置
        for i in range(len(s) - len(t) + 1):
            if s[i] == t[0]:
                fun(s[i+1:], t[1:], count)
    count = [0]
    fun(s, t, count)
    return count[0]

def numDistinct2(s: str, t: str) -> int:
    """
    动态规划。
    维护一个二维矩阵 dp，大小为 (m+1)*(n+1)，m为t的长度，n为s的长度
    dp[i][j] 表示 (s的前j个字符构成的字符串) 的所有子序列中等于 (t的前i个字符构成的字符串) 的个数。
    递推式：
                { dp[i][j-1], if s第j个字符 != t第i个字符
    dp[i][j] =  {
                { dp[i][j-1] + dp[i-1][j-1], else
    """
    m = len(t)
    n = len(s)
    dp = [[0] * (n+1) for x in range(m+1)]
    for j in range(n+1): # 第一行全部为 1
        dp[0][j] = 1
    for i in range(m):
        for j in range(n):
            if s[j] == t[i]:
                dp[i+1][j+1] = dp[i+1][j] + dp[i][j]
            else:
                dp[i+1][j+1] = dp[i+1][j]
    return dp[m][n]

if '__main__' == __name__:
    s = "rabbbit"
    t = "rabbit"
    print(numDistinct2(s,t))

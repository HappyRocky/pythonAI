# -*- coding: utf-8 -*-

"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

给定s1，s2，s3，判断 s3 是否是s1和s2的交错组成。

定义：若s1中属于s1的字符仍然保持在s1中原来的顺序，属于s2的字符仍然保持在s2中原来的顺序，则称s3是s1和s2的交错组成。

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""

def isInterleave(s1: str, s2: str, s3: str) -> bool:
    """
    动态规划。
    如果 s3 的前 k-1 个字符，是由 s1 的前 i 个字符和 s2 的前 j 个字符交错组成的，
    那么 s3 的第 k 个字符，应该是 s1 的第 i+1 个字符，或者是 s2 的第 j+1 个字符。
    记 dp[i][j] 表示 s3 的前 i+j 个字符，是否可以由 s1前i个字符 和 s2前j个字符 交错组成，是则为1，否则为0.
    状态转移方程：
                { 1, if (dp[i-1][j] == 1 and s1第i字符 == s3第i+j字符 or (dp[i][j-1] == 1 and s2第j字符 == s3第i+j字符)
    dp[i][j] =  {
                { 0, else
                
    最后 dp 矩阵的右下角，即为最后结果。
    """
    # 粗略判断
    m = len(s1)
    n = len(s2)
    if m == 0:
        return s2 == s3
    if n == 0:
        return s1 == s3
    if m + n != len(s3):
        return False
    # 初始化dp
    dp = [[False] * (n+1) for x in range(m+1)]
    for i in range(1, n+1): # 第一行，只有s2贡献字符
        dp[0][i] = s2[:i] == s3[:i]
    for i in range(1, m+1): # 第一列，只有s1贡献字符
        dp[i][0] = s1[:i] == s3[:i]
    # 动态规划
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1]and s2[j-1] == s3[i+j-1])
    return dp[i][j]

if '__main__' == __name__:
    s1 = "a"
    s2 = "b"
    s3 = "ab"
    print(isInterleave(s1, s2, s3))
        
        
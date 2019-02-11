# -*- coding: utf-8 -*-

'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character

给定两个单词 word1 和 word2，找到将 word1 转化为 word2 所需的最少操作步数。
对一个单词可以执行以下三种操作：
1、插入一个字符
2、删除一个字符
3、替换一个字符

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''

def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    动态规划。
    设 D(i,j) 为 word1 前i个字符和 word2 前j个字符的编辑距离。
    那么有递推关系式：
                [ D(i-1,j) + 1   
    D(i,j)= min [ D(i,j-1) + 1
                [ D(i-1,j-1) + [ 0, if word1第i个字符 == word2第j个字符
                               [ 1, else.
    我们要求的是 D(m,n)，其中m和n分别为word1和word2的长度。
    """
    m = len(word1)
    n = len(word2)
    # 初始化，D(i,0)=i, D(0,j)=j
    D = [[0] * (n+1) for _ in range(m+1)]
    D[0] = [i for i in range(n+1)]
    for i in range(m+1):
        D[i][0] = i
    # 迭代
    for i in range(1,m+1):
        for j in range(1,n+1):
            tmp1 = min(D[i-1][j], D[i][j-1]) + 1
            tmp2 = D[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1)
            D[i][j] = min(tmp1, tmp2)
    return D[m][n]

if '__main__' == __name__:
    word1 = "intention"
    word2 = ""
    print(minDistance(word1, word2))
    
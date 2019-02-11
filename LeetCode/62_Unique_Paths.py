# -*- coding: utf-8 -*-

'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
Note: m and n will be at most 100.

一个机器人位于一个m*n的网格的左上角。
它每次只能向下或向右移动一格。它试图到达网格的右下角。
求有多少种不重复的路径？
备注：
m和n最大为100.

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28
'''
import math
def uniquePaths1(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    数学法。
    路径数是可以通过数学公式直接计算出来的。
    对于m*n的网格，从左上角到右下角，无论怎么走，都必定包含m-1次右移和n-1次下移。
    因此问题转换为：将m-1个黑球和n-1个白球串成长度为 m+n-2 的队列，问排列方式有几种。
    思路：从 m+n-2 个空位置中，选出 m-1 个位置，放黑球，其他位置放白球。
    因此排列方式有 C_{m+n-2}^{m-1} = (m+n-2)! / ((m-1)!(n-1)!) 种。
    """
    return int(math.factorial(m+n-2) / math.factorial(m-1) / math.factorial(n-1))

def uniquePaths2(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    动态规划。
    设左上角坐标为(0,0)，右下角坐标为(m,n)。
    则走到(m,n)的路径数 = 走到(m-1,n)的路径数 + 走到(m,n-1)的路径数。
    这是因为
    1、要想走到(m,n)，必定会经过(m-1,n)或(m,n-1)的其中一个，因此需要相加。
    2、经过其中一个之后，只有一种走法可以到达终点，没有其他选择，因此不用乘以系数。
    3、经过其中一个之后，必定不会经过另外一个，不会有重叠，因此不用减去他们的交集。
    """
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]
    

if '__main__' == __name__:
    m, n = 7, 3
    print(uniquePaths2(m, n))
    

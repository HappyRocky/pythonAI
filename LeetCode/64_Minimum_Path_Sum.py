# -*- coding: utf-8 -*-

'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

给定一个 m*n 的非负整数矩阵，找到一条路径，从左上角到右下角，要求这条路径上的所有数组之和最小。
备注：每次只能向下或向右移动。

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    动态规划。
    将从左上角到坐标(i,j)的路径最小和为 dp(i,j)，则
    dp(i,j) = min(dp(i-1,j), dp(i,j-1)) + grid[i][j]
    """
    if not grid:
        return 0
    m = len(grid)
    n = len(grid[0])
    dp = [[x for x in grid[i]] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[i][j] += dp[i][j-1]
            elif j == 0:
                dp[i][j] += dp[i-1][j]
            else:
                dp[i][j] += min(dp[i][j-1], dp[i-1][j])
    return dp[-1][-1]

if '__main__' == __name__:
    grid = [
            [1,3,1],
            [1,5,1],
            [4,2,1]
            ]
    print(minPathSum(grid))
            
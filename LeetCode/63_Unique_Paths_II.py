# -*- coding: utf-8 -*-

'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?

一个机器人位于一个m*n的网格的左上角。
它每次只能向下或向右移动一格。它试图到达网格的右下角。
网格中有一些障碍物，机器人不能通过。
求有多少种不重复的路径？

备注：
1、m 和 n 都不大于 100.
2、障碍物和空地分别被标为 1 和 0。

Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''

def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    if not obstacleGrid or obstacleGrid[0][0] == 1:
        return 0
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1 # 起始点，一种路径
    for i in range(0, m):
        for j in range(0, n):
            if obstacleGrid[i][j] == 0: # 当前位置没有障碍物
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]   
    return dp[-1][-1]
    
if '__main__' == __name__:
    obstacleGrid = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
            ]
    print(uniquePathsWithObstacles(obstacleGrid))
    
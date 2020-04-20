# -*- coding: utf-8 -*-

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

给定一个三角形，找到从顶到底的最小路径和。每一步可以移动到相邻的下一行元素。

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

def minimumTotal(triangle: list) -> int:
    """
    从底向上考虑，一个节点距离最底部的最短路径，仅仅取决于其两个子节点距离最底部的最短路径。
    """
    dist_list = triangle[-1] # 最后一行
    for r in range(len(triangle) - 2, -1, -1): # 从倒数第二行开始向上遍历
        for i in range(r + 1):
            dist_list[i] = triangle[r][i] + min(dist_list[i], dist_list[i + 1])
    return dist_list[0]

if '__main__' == __name__:
    triangle = [[-1],
               [2,3],
             [1,-1,-3]]
    print(minimumTotal(triangle))

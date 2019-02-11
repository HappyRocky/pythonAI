# -*- coding: utf-8 -*-

'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

给定一个m*n的矩阵，如果一个元素是0，那么将其整行和整列都设置为0。
在原矩阵中操作。

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
'''

def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    zero_set1 = set() # 存放哪几行需要置零
    zero_set2 = set() # 存放哪几列需要置零
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_set1.add(i)
                zero_set2.add(j)
                
    # 对行和列置零
    for i in zero_set1:
        matrix[i] = [0]*n
    for j in zero_set2:
        for i in range(m):
            matrix[i][j] = 0

if '__main__' == __name__:
    matrix = [
            [0,1,2,0],
            [3,4,5,2],
            [1,3,1,5]
            ]
    setZeroes(matrix)
    print(matrix)
    
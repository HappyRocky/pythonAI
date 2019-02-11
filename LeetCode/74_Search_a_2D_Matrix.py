# -*- coding: utf-8 -*-

'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

实现一个有效算法，判断一个m*n的矩阵中是否存在某个值。
这个矩阵的特点：
1、每一行的整数值从左到右都是排好序的。
2、每一行中，第一个整数值比最后一个整数值大。

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''
def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    递归，二分法查找每一行。
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    row = matrix[0]
    # 目标值不在第一行，递归判断剩余行
    if target < row[0] or target > row[-1]:
        return searchMatrix(matrix[1:], target)
    # 二分查找
    l = 0
    u = len(row) - 1
    while(u >= l):
        mid = (l+u)//2
        if row[mid] == target:
            return True
        if row[mid] > target:
            u = mid - 1
        else:
            l = mid + 1
    return searchMatrix(matrix[1:], target)

if '__main__' == __name__:
    matrix = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
            ]
    target = 7
    print(searchMatrix(matrix, target))
    
    
    
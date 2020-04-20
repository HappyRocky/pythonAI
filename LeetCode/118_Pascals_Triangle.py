# -*- coding: utf-8 -*-

"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

给定一个非负整数 numRows，生成杨辉三角形的前 numRows 行。
在杨辉三角形中，每个元素等于它上面两个元素之和。

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""

def generate(numRows: int) -> list:
    """
    按照定义生成即可。
    最边上的元素均为1.
    """
    result = []
    for r in range(numRows):
        row = [1] * (r + 1)
        for i in range(1, r):
            row[i] = result[-1][i-1] + result[-1][i]
        result.append(row)
    return result

if '__main__' == __name__:
    print(generate(5))
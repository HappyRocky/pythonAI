# -*- coding: utf-8 -*-

"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

给定一个非负索引k，k<=33，返回杨辉三角形的第k行。
行索引从0开始。

Example:
Input: 3
Output: [1,3,3,1]

"""

def getRow(rowIndex: int) -> list:
    """
    按照定义，不断延长row，直至到目标行。
    """
    row = [1]
    for r in range(rowIndex):
        pre = 1
        for i in range(1, len(row)):
            cur = row[i]
            row[i] = cur + pre
            pre = cur
        row.append(1)
    return row

if '__main__' == __name__:
    print(getRow(2))

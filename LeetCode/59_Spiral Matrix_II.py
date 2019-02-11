# -*- coding: utf-8 -*-

'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

给定一个正整数 n，生成一个方阵，里面的元素为1到n^2按照螺旋顺序排列。

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    分治法。
    按照定义，从左上角开始，依次按照顺序生成1到n^2的数。
    每次生成最外圈，然后递归生成剩余元素。
    """
    board = [[0 for i in range(n)] for i in range(n)]
    
    def generate(k, nextvalue):
        '''
        生成第k个外圈以及内部所有元素。
        '''
        nonlocal board
        # 计算最外圈的两行两列位置
        minr = k-1 # 上行、左列
        maxr = n-k # 下行、右列
        # 递归结束条件
        if minr > maxr:
            return
        if minr == maxr:
            board[minr][minr] = nextvalue
            return
        # 开始生成最外圈
        for i in range(4): # 逆时针旋转4次
            # 最上面一行赋值
            board[minr][minr:maxr] = list(range(nextvalue, nextvalue + maxr - minr))
            nextvalue = board[minr][maxr-1] + 1
            board = [list(x) for x in zip(*board)][::-1] # 逆时针旋转
        # 递归生成里面的圈
        generate(k+1, nextvalue)
    
    generate(1, 1)
    return board

if '__main__' == __name__:
    n = 3
    print(generateMatrix(n))
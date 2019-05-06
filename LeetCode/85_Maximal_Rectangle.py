# -*- coding: utf-8 -*-

'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

给定一个2维二进制矩阵，元素为0或1。返回只包含1的最大矩阵面积。

Example:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''

def maximalRectangle(matrix: 'List[List[str]]') -> 'int':
    '''
    可以借鉴第84题：寻找柱状图中的最大矩形面积。本题每一列可以看做一个柱子。
    不过，84题的柱子底部都是平齐的，但是本题的柱子是不平齐的，甚至每一列有多个柱子(1表示柱子)。
    因此，可以逐行遍历，依次将前1行、前2行、... 当做一道第84题，进行最大面积的计算。
    比如示例，可以先看第一行：
    ["1","0","1","0","0"]
    柱子的长度分别为 1、0、1、0、0，最大面积为1.
    再看前2行：
    ["1","0","1","0","0"],
    ["1","0","1","1","1"]
    柱子的长度分别为：2、0、2、1、1，最大面积为3.
    再看前3行：
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    柱子的长度分别为：3、1、3、2、2，最大面积为6.    
    再看前4行：
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]    
    柱子的长度分别为：4、0、0、3、0，最大面积为4.
    综上：本题的最大面积为6.
    注意：只要柱子的最底部为0，那么无论上面有多少1，这根柱子的高度都是0。
    '''
    if not matrix or not matrix[0]:
        return 0
    
    m = len(matrix)
    n = len(matrix[0])
    heights = [0] * (n + 1) # 每一个柱子的高度
    max_area = 0 # 存放历史最大面积
    for i in range(m):
        stack = list()
        for j in range(n+1):
            # 更新heights
            if j < n:
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            # 判断与栈顶柱高的大小
            while(stack and heights[j] < heights[stack[-1]]):
                top = stack.pop()
                if stack:
                    cur_area = heights[top] * (j - 1 - stack[-1])
                else:
                    cur_area = heights[top] * j
                max_area = max(max_area, cur_area)
            if (not stack) or heights[j] >= heights[stack[-1]]: # 递增，压入栈
                stack.append(j)
    return max_area

if '__main__' == __name__:
    matrix = [
            ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]
            ]
    print(maximalRectangle(matrix))
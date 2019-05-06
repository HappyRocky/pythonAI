# -*- coding: utf-8 -*-

'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

给定 n 个非负整数，代表柱状图中的柱高，每个柱子宽度为1。要求找到柱状图中最大的矩形面积。

Example:
Input: [2,1,5,6,2,3]
Output: 10
'''

def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    定义一个栈，从左到右遍历数组，如果元素大小比栈顶的大，则压入栈，继续遍历。
    否则，弹出栈顶元素，并计算栈顶坐标和当前坐标之间的容量，取较大者。
    这样，可以保证，每次遇到一个较短的柱子，可以计算出它与之前所有柱子中最大的矩形面积。
    注意，在最后要追加一个高度为0的柱子，这样可以保证比前一个柱子短。
    """
    heights.append(0) # 末尾追加0，保证进入下面的else块
    n = len(heights)
    stack = list()
    max_area = 0 # 存放历史最大面积
    i = 0
    while i < n:
        if (not stack) or heights[i] > heights[stack[-1]]: # 递增，压入栈
            stack.append(i)
            i += 1
        else: # 遇到较短柱子，则计算stack中以top为末尾的柱子们之间的最大面积
            top = stack.pop()
            if stack:
                cur_area = heights[top] * (i - stack[-1] - 1)
            else:
                cur_area = heights[top] * i
            max_area = max(max_area, cur_area)
    return max_area

if '__main__' == __name__:
    heights = [2,1,5,6,2,3]
    print(largestRectangleArea(heights))
    
    
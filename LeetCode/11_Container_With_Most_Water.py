# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 10:19:15 2018

@author: gongyanshang1

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.

给定n个非负整数a1,a2,...,an，每个整数对应一个坐标为(i, ai)的点。
这样形成了n条竖直的线段，线段的两个端点分别为 (i, ai) 和 (i, 0)。
要求找到两条线段，使得他们与x轴组成的容器可以盛最多的水，并输出最大容量。
备注：不可以倾斜容器，且 n 至少为 2.

示例：
Input: [1,8,6,2,5,4,8,3,7]
在第2根线（8）与最后一根线（7）之间的容量最大，容量为 min(8, 7) * 7 = 49。
Output: 49

"""

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    从两边往中间寻找。
    """
    
    max_area = 0
    l = 0
    r = len(height) - 1
    while(l < r):
        max_area = max(max_area, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area

if '__main__' == __name__:
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))
    
    

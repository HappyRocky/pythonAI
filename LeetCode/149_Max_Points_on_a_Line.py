# -*- coding: utf-8 -*-

"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

给定2D平面内的 n 个点，找到在同一条直线中包含点数的最大值。

Example 1:
Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4

Example 2:
Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

def maxPoints(points: list) -> int:
    """
    固定一个点，查看其它点与这个点的斜率，所有相同斜率的点都在一条直线上。
    """
    def slope(i, j):
        """
        计算points[i]和points[j]两个点的斜率，无穷大则返回'i'
        """
        if points[i][0] == points[j][0]:
            return 'i'
        
        def frac(x, y):
            """
            求x除以y的结果，但不是返回float，而是返回 x//g, y//g，其中 g 是最大公约数。
            """
            def gcd(a, b):
                if b == 0:
                    return a
                return gcd(b, a % b)
            g = gcd(x, y)
            return x // g, y // g
        
        return frac(points[i][1] - points[j][1], points[i][0] - points[j][0])
        
    if not points:
        return 0
    n = len(points)
    if n <= 2:
        return n
    # 遍历每个点
    result = 1
    for i in range(n-1):
        dic = {'i':1} # <斜率:点数>，i表示斜率为无穷大，即竖直的线
        same = 0 # 重合的点数
        for j in range(i+1, n):
            if points[i] == points[j]:
                same += 1
            else:
                s = slope(i, j)
                dic[s] = dic.get(s, 1) + 1
        result = max(result, max(dic.values()) + same)
    return result

if '__main__' == __name__:
    points = [[0,0],[94911151,94911150],[94911152,94911151]]
    print(maxPoints(points))
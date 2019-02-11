# -*- coding: utf-8 -*-

'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

给定一个矩阵 m*n，返回所有元素的螺旋排列顺序。

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    递归法。
    先输出最外圈的顺时针顺序，然后用同样方法处理剩下的元素。
    """
    
    # 递归结束条件
    if not matrix or len(matrix[0]) == 0:
        return []
    if len(matrix) == 1: # 只有一行
        return matrix[0]
    if len(matrix[0]) == 1: # 只有一列
        return [x[0] for x in matrix]
    
    # 最外圈的螺旋排列
    result = matrix[0] # 第一行
    result += [x[-1] for x in matrix][1:-1] # 最后一列
    result +=  matrix[-1][::-1] # 最后一行
    result += [x[0] for x in matrix][-2:0:-1]  # 第一列
    
    # 切割出剩余元素
    remain = [matrix[i][1:-1] for i in range(1,len(matrix)-1)]
    
    return result + spiralOrder(remain)

def spiralOrder2(matrix):
    '''
    递归法，一行代码。
    每次递归，输出第一行，然后将矩阵逆时针旋转90度。
    备注：当 matrix = [] 时，matrix and [*matrix.pop(0)] 这个表达式返回 []，
    这是因为 and 符号连接时，先计算左边的正负，时，matrix 为空，为FALSE，因此不必再计算 and 右边的表达式。
    直接返回 matrix，即 []。
    * 后面加上可迭代对象，相当于将可迭代对象变为list，并列出。
    可以用在两个场合：
    1、[*a] 表示将a变为list，相当于 list(a)
    2、fun(*a) 表示将a变为list，并且每个元素分别作为fun()的一个参数，即这时 fun 被传入了多个参数，而不是一个。
    比如：
    >>> matrix = [1,2,3]
    >>> type(*matrix)
    Traceback (most recent call last):
        File "<ipython-input-283-d63d2bd0f73e>", line 1, in <module>
            type(*matrix)
    TypeError: type.__new__() argument 1 must be str, not int
    
    相当于执行了 type(1,2,3)，因此会报错。
    '''
    return matrix and [*matrix.pop(0)] + spiralOrder2([*zip(*matrix)][::-1])

if '__main__' == __name__:
    matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
    print(spiralOrder2(matrix))
    
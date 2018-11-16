# -*- coding: utf-8 -*-

'''
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

给定一个 n*n 的二维矩阵，表示一副图像。
将图像顺时针旋转90度。

备注：
只能直接修改原矩阵，不能创建其他的二维矩阵。

Example 1:
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 
rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    
    旋转规律：
    矩阵的 (i,j) 旋转90度会转到位置 (j,n-1-i)。
    但是，如果直接将 (i,j) 的值赋给 (j, n-1-i)，那么需要提前将 (j, n-1-i) 的值保存起来，
    然后赋给它的旋转位置 (n-1-i, n-1-j)。
    继续循环，后面的位置依次为 (n-1-j, i)、(i, j)。
    即旋转四次会回到原位置。
    这样，就完成了这4个位置的旋转。
    然后继续遍历，完成其他位置的旋转。
    """
    
    n = len(matrix)
    locate_set = set() # 存放已经旋转过的位置
    for i in range(n):
        for j in range(n):
            if (i,j) not in locate_set:
                ii, jj, tmp = i, j, matrix[i][j]
                for _ in range(4):
                    locate_set.add((ii, jj))
                    # 当前值赋给旋转之后的位置
                    next_ii, next_jj = jj, n-1-ii
                    tmp1 = matrix[next_ii][next_jj]
                    matrix[next_ii][next_jj] = tmp
                    # 继续下一个位置的旋转
                    ii, jj, tmp = next_ii, next_jj, tmp1
                    
def rotate2(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.  
    另一个旋转规律：
    顺时针旋转90度 = 先沿左上-右下的对角线进行对称，再将每一行进行反转。
    """                  
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i] = matrix[i][::-1]

def output_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
            
if '__main__' == __name__:
    matrix = [
            [ 5, 1, 9,11],
            [ 2, 4, 8,10],
            [13, 3, 6, 7],
            [15,14,12,16]
            ]
    print('原矩阵：')
    output_matrix(matrix)
    rotate2(matrix)
    print('旋转90度之后：')
    output_matrix(matrix)
                    
                    
                    
                    
    
    
# -*- coding: utf-8 -*-

'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

n皇后问题需要将n个皇后放置在n*n的棋盘上，保证任意两个皇后都不能处于同一行、同一列或同一斜线上。
给定一个整数n，返回n皇后问题的所有不重复的解的个数。

Example:
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

def totalNQueens(n):
    """
    :type n: int
    :rtype: int
    回溯法。
    """
    count = 0
    def place_queen(place_list, cur_row):
        '''
        在第 cur_row 行上放置一个皇后。
        place_list:长度为n，每一个元素代表这一行上的皇后的位置
        '''
        nonlocal count
        # 递归结束条件
        if cur_row == len(place_list):
            count += 1
            return
        
        # 在cur_row这一行上对所有位置依次尝试放置皇后
        for cur_col in range(n):
            place_list[cur_row] = cur_col
            
            # 判断是否有同行同列同斜边的皇后
            for row in range(cur_row):
                col = place_list[row]
                if col == cur_col or abs(cur_col - col) == cur_row - row:
                    break
            else:
                # 没有break，说明有效，继续放置下一行
                place_queen(place_list, cur_row + 1)
    
    place_queen([0] * n, 0)
    return count

if '__main__' == __name__:
    n = 4
    print(totalNQueens(n))

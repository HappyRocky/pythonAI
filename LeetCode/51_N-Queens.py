# -*- coding: utf-8 -*-

'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

n皇后问题需要将n个皇后放置在n*n的棋盘上，保证任意两个皇后都不能处于同一行、同一列或同一斜线上。
给定一个整数n，返回n皇后问题的所有不重复的解。
每个解都是一种n个皇后的布局，其中 'Q' 和 '.' 分别代表皇后和空白。

Example:
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''
def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    回溯法。
    """
    
    def place_queen(result_list, place_list, cur_row):
        '''
        在第 cur_row 行上放置一个皇后。
        result_list:存放所有的解
        place_list:长度为n，每一个元素代表这一行上的皇后的位置
        '''
        
        # 递归结束条件
        if cur_row == len(place_list):
            # 将答案转为二维棋盘，放入到result_list中
            result_list.append(['.'*i + 'Q' + '.'*(n-i-1) for i in place_list])
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
                place_queen(result_list, place_list, cur_row + 1)
    
    result_list = []
    place_queen(result_list, [0] * n, 0)
    return result_list

def output_board(board_list):
    '''
    输出棋盘
    '''
    print(f'共{len(board_list)}种解法')
    for board in board_list:
        print(' ')
        for row in board:
            print(row)

if '__main__' == __name__:
    n = 4
    output_board(solveNQueens(n))
                    
            
        
    
    
    
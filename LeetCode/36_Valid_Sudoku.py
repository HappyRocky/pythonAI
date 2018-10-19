# -*- coding: utf-8 -*-

'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.

判断一个 9*9 的数独面板是否是有效的。
如果已经被填充的数字满足以下条件，则说明是有效的：
1、每一行一定要包含无重复数字1-9
2、每一列一定要包含无重复数字1-9
3、每一个 3*3 的子面板一定要包含无重复数字1-9

备注：
1、一个有效的数独面板（部分填充）不必是可解的
2、只要被填充的数字满足有效条件即可
3、数独面板可以只被部分填充，其他空缺的为字符'.'
4、面板只能包含数字1-9或者字符'.'
5、面板大小总是 9*9

Example 1:
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

'''

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    依次判断3个有效条件是否全部满足。
    """
    
    def is_row_valid(board):
        '''
        判断一个数独的每一行是否都包含无重复数字1-9
        '''
        for row in board:
            char_set = set()
            for char in row:
                if char != '.':
                    if char in char_set:
                        return False
                    char_set.add(char)
        return True
    
    # 1、每一行一定要包含无重复数字1-9
    if not is_row_valid(board):
        return False
                
    # 2、每一列一定要包含无重复数字1-9
    board_reverse = [[board[i][j] for i in range(9)] for j in range(9)]
    if not is_row_valid(board_reverse):
        return False    
    
    # 3、每一个 3*3 的子面板一定要包含无重复数字1-9
    for i in range(3):
        for j in range(3):
            char_set = set()
            for ii in range(i*3, (i+1)*3):
                for jj in range(j*3, (j+1)*3):
                    char = board[ii][jj]
                    if char != '.':
                        if char in char_set:
                            return False
                        char_set.add(char)
    return True

def isValidSudoku2(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    一次遍历，同时判断是否满足3个有效条件。
    """
    
    char_set = set()
    for i in range(9):
        for j in range(9):
            char = board[i][j]
            if char != '.':
                if (i, char) in char_set \
                    or (char, j) in char_set \
                    or (i//3, j//3, char) in char_set:
                        return False
                else:
                    char_set.add((i, char)) # 第i行的char字符
                    char_set.add((char, j))  # 第j列的char字符
                    char_set.add((i//3, j//3, char)) # [i//3, j//3]位置的小面板的char字符
    return True

if '__main__' == __name__:
    board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    print(isValidSudoku2(board))
    
# -*- coding: utf-8 -*-

'''
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

给定一个二维面板和一个单词，判断单词是否存在于面板中。
单词需要按照相邻字符的顺序来构建，相邻指的是上下左右的邻近。同一个字符不能使用超过一次。

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    回溯法。
    遍历board，直至找到能匹配word第一个字符的位置，然后使用递归法继续寻找这个位置的上下左右四个位置是否能匹配word第二个字符，同时将这个位置标为已使用。
    如果不能匹配，则将这个位置的状态回溯为未使用，继续递归下一个字符。
    """
    def select(board, used_board, i, j, word, cur_idx):
        '''
        面板中是否存在word[cur_idx],从borad[i,j]开始寻找
        '''
        # 越界
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False
        # 当前位置可以匹配word字符
        if board[i][j] == word[cur_idx] and used_board[i][j] == 0:
            # 寻找完毕
            if cur_idx == len(word) - 1:
                return True
            # 没有寻找完毕，递归寻找后面的字符
            used_board[i][j] = 1 # 表示已经使用过这个位置
            result = select(board, used_board, i-1, j, word, cur_idx+1)\
                    or select(board, used_board, i+1, j, word, cur_idx+1)\
                    or select(board, used_board, i, j-1, word, cur_idx+1)\
                    or select(board, used_board, i, j+1, word, cur_idx+1)
            if result:
                return True
            # 回溯
            used_board[i][j] = 0
        # 如果是第一个字符，则继续寻找下一个
        if cur_idx == 0:
            # 获取下个位置的坐标，从上到下，从左到右
            if j == len(board[0])-1:
                j = 0
                i += 1
                if i == len(board):
                    return False
            else:
                j += 1
            return select(board, used_board, i, j, word, cur_idx)
        else:
            return False
    used_board = [[0] * len(board[0]) for x in range(len(board))]
    return select(board, used_board, 0, 0, word, 0)

def exist2(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    回溯法的改良版。
    1、如果是第一个字符，则继续寻找下一个。这个逻辑可以不放到递归函数中，而是放在主流程中，用双层循环表示。
    2、可以不定义used_board，直接修改board本身为#号，回溯时再改回来。
    """
    def select(board, i, j, word, cur_idx):
        '''
        面板中是否存在word[cur_idx],从borad[i,j]开始寻找
        '''
        # 越界
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False
        # 当前位置可以匹配word字符
        if board[i][j] == word[cur_idx]:
            # 寻找完毕
            if cur_idx == len(word) - 1:
                return True
            # 没有寻找完毕，递归寻找后面的字符
            tmp, board[i][j] = board[i][j], '#'
            result = select(board,i-1, j, word, cur_idx+1)\
                    or select(board, i+1, j, word, cur_idx+1)\
                    or select(board, i, j-1, word, cur_idx+1)\
                    or select(board, i, j+1, word, cur_idx+1)
            if result:
                return True
            # 回溯
            board[i][j] = tmp
        return False
    
    # 遍历
    for i in range(len(board)):
        for j in range(len(board[0])):
            if select(board, i, j, word, 0):
                return True
    return False

if '__main__' == __name__:
    word = "eat"
    board = [
            ['o','a','a','n'],
            ['e','t','a','e'],
            ['i','h','k','r'],
            ['i','f','l','v']
            ]
    print(exist(board, word))
            
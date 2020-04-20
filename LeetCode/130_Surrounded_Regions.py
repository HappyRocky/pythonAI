# -*- coding: utf-8 -*-

"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

给定一个二维面板，包含'X'和'O'，寻找所有被'X'包围的区域，将里面的'O'变为'X'。
备注：
1、这种区域不能包含斌姐，即边界上的任何'O'不会被转为'X'。
2、任何不在边界且不和边界上的'O'相连接的'O'，都应该被转为'X'。
3、两个单元相连接，指的是他们在水平或竖直方向上相邻。


Example:
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X
Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""

def solve(board: list) -> None:
    """
    寻找所有能够与边界相连接的'O'并标记。
    然后除了这些'0'之外的所有'O'都转为'X'
    """
    if not board or len(board) <= 2 or len(board[0]) <= 2:
        return
    m, n = len(board), len(board[0])
    # 寻找与边界连通的'O'
    border_set = set() # 存放与边界连通的'O'的坐标
    stack = list() # 存放'O'的候选者
    # 初始化stack，将四个边界的'O'放进去
    for i in range(n):
        if board[0][i] == 'O':
            stack.append((0, i))
        if board[m-1][i] == 'O':
            stack.append((m - 1, i))
    for i in range(1, m-1):
        if board[i][0] == 'O':
            stack.append((i, 0))
        if board[i][-1] == 'O':
            stack.append((i, n - 1))
    # 开始扫描stack
    while(stack):
        i, j = stack.pop()
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O' and (i, j) not in border_set:
            border_set.add((i, j))
            # 将相邻的'0'压入栈
            stack.append((i + 1, j))
            stack.append((i - 1, j))
            stack.append((i, j + 1))
            stack.append((i, j - 1))
    # 扫描面板，转换'O'
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if board[i][j] == 'O' and (i, j) not in border_set:
                board[i][j] = 'X'

if '__main__' == __name__:
    board = [["O","X","O","O","X","X"],
             ["O","X","X","X","O","X"],
             ["X","O","O","X","O","O"],
             ["X","O","X","X","X","X"],
             ["O","O","X","O","X","X"],
             ["X","X","O","O","O","O"]]
    solve(board)
    print(board)
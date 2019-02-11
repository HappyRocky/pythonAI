# -*- coding: utf-8 -*-

'''
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

给定一个二维面板和一个单词列表，找到存在于面板中的所有单词。
单词需要按照相邻字符的顺序来构建，相邻指的是上下左右的邻近。同一个字符不能使用超过一次。

Example:
Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Output: ["eat","oath"]
'''
class CharNode: # 链表类
    def __init__(self):
        self.word = None
        self.next = dict()
    
def findWords(board, words):
    """
    :type board: List[List[str]]
    :type words: List[str]
    :rtype: List[str]
    定义一个链表，将words中的所有单词都存储到链表中，每个节点代表一个字符。
    这样，重复的单词或者A是B的子串的情况就只会扫描一次，提高效率。
    使用递归回溯法，将board遍历一遍，判断从每个位置出发，其相邻位置是否可以凑成链表中的单词。
    """
    def select(result_list, board, i, j, char_node):
        '''
        递归，从borad[i,j]开始寻找char_node中符合条件的word
        '''
        # 越界
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return
        c = board[i][j]
        # 没有匹配的字符
        if c not in char_node.next:
            return
        # 是否到达末尾
        char_node = char_node.next[c]
        if char_node.word: # 到达末尾
            result_list.append(char_node.word)
            char_node.word = None # 防止重复
        # 继续寻找
        board[i][j] = '#'
        select(result_list, board, i-1, j, char_node)
        select(result_list, board, i+1, j, char_node)
        select(result_list, board, i, j-1, char_node)
        select(result_list, board, i, j+1, char_node)
        board[i][j] = c # 回溯    

    # 构造链表
    char_node = CharNode()
    for word in words:
        p = char_node
        for c in word:
            if c not in p.next:
                p.next[c] = CharNode()
            p = p.next[c]
        p.word = word # 末尾节点附上word
    
    # 遍历
    result_list = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            select(result_list, board, i, j, char_node)
    return sorted(result_list)

if '__main__' == __name__:
    board = [["s","e","e","n","e","w"],["t","m","r","i","v","a"],["o","b","s","i","b","d"],["w","m","y","s","e","n"],["l","t","s","n","s","a"],["i","e","z","l","g","n"]]
    words = ['bend','benda','work']
    print(findWords(board, words))

    
    

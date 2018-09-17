# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 10:41:46 2018

@author: gongyanshang1

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

给定整数n，要求输出 n 对左右括号的所有可能的有效组合。

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    递归法。
    """
    
    def fun_rec(left_count, right_count):
        '''
        将left_count个左括号和right_count右括号进行有效组合
        '''
        if left_count == 0 and right_count == 0:
            return ['']
        if left_count == 0:
            return [''.join([')'] * right_count)]
        if right_count == 0:
            return [''.join([')'] * right_count)]
        if left_count == right_count: # 左右数量相等时，只能先放左括号
            remain_list = fun_rec(left_count - 1, right_count)
            return ['(' + x for x in remain_list]
        else: # 左括号少于右括号（不可能大于），则左右括号都可以放
            remain_list = fun_rec(left_count - 1, right_count)
            l1 = ['(' + x for x in remain_list]
            remain_list = fun_rec(left_count, right_count - 1)
            l2 = [')' + x for x in remain_list]
            return l1 + l2
        
    return fun_rec(n, n)

if '__main__' == __name__:
    n = 3
    print(generateParenthesis(n))
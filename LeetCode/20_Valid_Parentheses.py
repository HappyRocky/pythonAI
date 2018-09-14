# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 09:44:07 2018

@author: gongyanshang1

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1.Open brackets must be closed by the same type of brackets.
2.Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

给定一个字符串，只包含字符'(', ')', '{', '}', '[' and ']'，判断此字符串是否有效。
满足以下条件为有效：
1、左括号必须有同样类型的右括号相匹配
2、右括号匹配顺序必须和左括号相对应

注意，一个空字符串也是有效的。

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true

"""

def isValid(s):
    """
    :type s: str
    :rtype: bool
    维护一个栈，每次遇到左括号便放进去，每次遇到右括号便pop一个左括号看是否与之对应。
    如果遍历完字符串后，栈变为空，则说明字符串是有效的。    
    """
    if not s:
        return True
    
    if len(s) % 2 == 1:
        return False
    
    left = {'(':')','{':'}','[':']'}
    stack = []
    for char in s:
        if char in left:
            stack.append(char)
        elif not stack or left[stack.pop()] != char:
            return False
    return not stack

if '__main__' == __name__:
    s = "([)]"
    print(isValid(s))
            
            
    


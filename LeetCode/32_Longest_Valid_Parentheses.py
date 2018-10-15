# -*- coding: utf-8 -*-

'''
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.

给定一个字符串，只包含'('和')'。
要求找到最长的有效的子串。

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

'''

def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    使用栈来判断一个子串是否是有效子串。
    构建多个栈，每个栈的作用是判断从当前字符开始到s结束的子串是否是有效子串。
    步骤：
    只需扫描一次，每扫描到一个字符，就比对所有的栈，看是否是有效子串。
    如果扫描到了左括号，还需要开辟一个新的栈。
    时间复杂度为O(n^2)。
    """
    
    if len(s) <= 1:
        return 0
    stack_list = [] # 每个元素为 (stack, start_idx)
    max_len = 0
    for i in range(len(s)):
        char = s[i]
        if char == '(':
            # 所有栈追加符号
            for stack in stack_list:
                stack[0].append(char)
            
            # 开辟一个新的栈
            stack_list.append(([char], i))
        else:
            for j in range(len(stack_list)-1, -1, -1):
                stack = stack_list[j]
                if not stack[0] or stack[0].pop() != '(':
                    del stack_list[j]
                    continue
                if not stack[0]: # 恰好栈变为空
                    max_len = max(max_len, i - stack[1] + 1)
    return max_len

def longestValidParentheses2(s):
    """
    :type s: str
    :rtype: int
    扫描一遍，构造一个栈，最后只剩下匹配不上的索引。
    不在栈内的索引是可以匹配上的，因此栈内相邻索引之间的子串为有效子串。
    相邻索引的差值，即为有效子串的长度。
    时间复杂度为 O(n)。
    """
    l = len(s)
    
    # 扫描一遍，构造一个栈，最后只剩下匹配不上的索引
    stack = []
    for i in range(l):
        if s[i] == ')' and stack and s[stack[-1]] == '(':
            stack.pop()
        else:
            stack.append(i)
    # 不在栈内的索引是可以匹配上的，统计其中的最长子串
    if not stack:
        return l
    stack.insert(0, -1)
    stack.append(l)
    return max(stack[i+1]-stack[i]-1 for i in range(len(stack)-1))
    
if '__main__' == __name__:
    s = ")"
    print(longestValidParentheses2(s))

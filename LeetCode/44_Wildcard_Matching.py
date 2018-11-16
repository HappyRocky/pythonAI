# -*- coding: utf-8 -*-

'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.

给定一个输入字符串s和一个模式字符串p，实现正则匹配，支持'?'和'*'。

'?' 可以匹配任何单个字符
'*' 可以匹配任何字符的序列（包括空序列）
需要匹配整个输入字符串 s，不能部分匹配。

备注：
s 只会包含小写 a-z，可以为空。
p 只会包含小写 a-z、? 或 *，可以为空。

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    if not p:
        return not s
    
    if s: # s不为空
        if p[0] in [s[0], '?']: # 首字符相同，或者p首字符为?，都可以匹配上
            return isMatch(s[1:], p[1:]) # 各右移一位，继续匹配
        elif p[0] == '*': # p首字符为*
            # isMatch(s[1:], p)试探让*表示s的首字符，s右移一位，*保留
            # isMatch(s, p[1:])试探让*表示空字符，略过*，s不变
            return isMatch(s[1:], p) or isMatch(s, p[1:]) 
    elif p[0] == '*': # s为空，则只有p全部为*，才可以匹配上
        return isMatch(s, p[1:])
    
    return False

def isMatch2(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    p.replace('**','*')
    memo = {}
    def dp(i, j):
        if (i, j) not in memo:
            ans = False
            if j == len(p):
                ans = i == len(s)
            elif i < len(s):
                if p[j] in [s[i], '?']:
                    ans = dp(i+1, j+1)
                elif p[j] == '*':
                    if (i, j+1) in memo:
                        ans = dp(i, j+1) or dp(i+1, j)
                    else:
                        ans = dp(i+1, j) or dp(i, j+1) 
            elif p[j] == '*':
                ans = dp(i, j+1)
            memo[i, j] = ans
        return memo[i, j]
    return dp(0, 0)      
    
if '__main__' == __name__:
    s = "adceb"
    p = "*a*b"
    print(isMatch(s, p))
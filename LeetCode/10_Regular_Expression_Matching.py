# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:41:29 2018

@author: gongyanshang1


Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

给定一个输入字符串s和一个模式字符串p，实现正则匹配，支持'.'和'*'。
'.'可以匹配任意单个字符。
'*'可以匹配0个或多个前一个元素。
匹配需要覆盖整个输入字符串，而非部分匹配。
备注：
s 可以为空，且只会包含小写字母 a-z
p 可以为空，且只会包含小写字母 a-z，以及 . 或者 *

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

"""

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    
    递归，从左至右判断。
    """
    
    if not p:
        return not s
    
    # 判断s的第一个字符是否可以匹配p的第一个字符
    first_match = bool(s) and p[0] in [s[0], '.']
    if len(p) >= 2 and p[1] == '*':
        return (first_match and isMatch(s[1:], p)) or isMatch(s, p[2:])
    else:
        return first_match and isMatch(s[1:], p[1:])
    
def isMatch2(text, pattern):
    """
    :type s: str
    :type p: str
    :rtype: bool
    
    递归，从左至右判断。
    与上面函数不同之处在于，将每次结果存储了下来，一旦之后再次用到，直接取出即可。
    这个方法的优势，在于 or 。一个or就将复杂度扩大为O(S^2)，因为最坏情况下，需要调用 1+2+4... 次递归函数。
    而加入存储方法之后，每次只需计算一遍。
    """
    memo = {}
    def dp(i, j):
        if (i, j) not in memo:
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    ans = dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    ans = first_match and dp(i+1, j+1)

            memo[i, j] = ans
        return memo[i, j]

    return dp(0, 0)
    
if '__main__' == __name__:
    s = 'aaaaaaaaaaaaab'
    p = "a*a*a*a*a*a*a*a*a*a*c"
    #print(isMatch(s,p))
    print(isMatch2(s,p))



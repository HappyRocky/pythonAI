# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 09:36:15 2018

@author: gongyanshang1

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

给定一个字符串s，找到s中最长的回文字字符串。假设s的最大长度为1000.

示例：
Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"

"""

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    
    暴力求解。扫描所有子字符串，分别判断是否为回文字符串，返回最长的回文字符串。
    时间复杂度为O(n^3)
    """
    
    def is_palindromic(a):
        '''
        a是否为回文字符串
        '''
        b = a[::-1]
        if a == b:
            return True
        return False
    
    max_substr = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j+1]
            if is_palindromic(substr) and len(substr) > len(max_substr):
                max_substr = substr
    return max_substr

def longestPalindrome2(s):
    """
    :type s: str
    :rtype: str
    
    暴力求解的优化：每次判断一个字符串是否是回文字符串时，p(s[i:j]) = p(s[i+1:j-1]) && s[i] == s[j]。
    将每次的判断结果存存起来，之后再用就不用重新计算了。
    但需要从后向前遍历，这样才会用得到提前存储的结果。
    时间复杂度为O(n^2)。
    """
    
    if len(s) <= 1:
        return s
    
    def is_palindromic(a, dic):
        '''
        a是否为回文字符串
        '''
        result = False
        if len(a) == 1:
            result = True
        elif len(a) == 2:
            result = a[0] == a[1]
        else:
            b = a[1:-1]
            if b in dic:
                result = dic[b] and a[0] == a[-1]
            else:
                b = a[::-1]
                if a == b:
                    result = True
        dic[a] = result
        return result
    
    max_substr = ''
    dic = dict()
    for i in range(len(s)-1, -1, -1):
        for j in range(i, len(s)):
            substr = s[i:j+1]
            if is_palindromic(substr, dic) and len(substr) > len(max_substr):
                max_substr = substr
    return max_substr

def longestPalindrome3(s):
    """
    :type s: str
    :rtype: str
    
    求原字符串和逆字符串的公共子串。
    1、求公共子串可以使用动态规划方法，详情见 https://github.com/HappyRocky/pythonAI/blob/master/algorithm-exercise/find_max_same_substring.py
    2、不是所有的公共子串都符合要求，还需要判断原字符串翻转之后是否还是同一个子串。
    时间复杂度为O(n^2)。
    """
    if len(s) <= 1:
        return s
    
    # 翻转
    s1 = s
    s2 = s[::-1]
    
    # 矩阵，高为s1长度，宽为s2长度
    flag_matrix = []
    max_len = 0
    last_idx = 0
    for i in range(len(s1)):
        flag_matrix.append([])
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i > 0 and j > 0:
                    flag_matrix[i].append(flag_matrix[i-1][j-1] + 1)
                else:
                    flag_matrix[i].append(1)
            else:
                flag_matrix[i].append(0)
            # 比已知的最大长度还长，且：s1中子串起始位置距离原字符串的起始位置 == s2中子串的末尾位置距离原字符串的末尾位置  
            if flag_matrix[i][j] > max_len and i - flag_matrix[i][j] + 1 == len(s2) - j - 1:
                max_len = max(max_len, flag_matrix[i][j])
                last_idx = i
    return s1[last_idx-max_len+1 : last_idx+1]

def longestPalindrome4(s):
    """
    :type s: str
    :rtype: str
    
    移动中心法。
    先假设某个位置为回文字符串的中心，然后查询以此位中心的最长回文字符串。遍历中心，即可找到全局最长子串。
    时间复杂度为O(n^2)。
    """
    if len(s) <= 1:
        return s
    
    max_str = ''
    
    # 枚举mid_idx。一个mid_id决定了两个中心位置：mid_idx本身、和右邻之间的分界线。
    for mid_idx in range(len(s)):
        
        # 以mid_idx为中心
        count = 0  # 从中心向两边慢慢扩张
        while(True):
            start_idx = mid_idx-count
            end_idx = mid_idx+count
            if s[start_idx] == s[end_idx]:
                count += 1
                if end_idx - start_idx + 1 > len(max_str):
                    max_str = s[start_idx:end_idx+1]
            else:
                break
            if start_idx == 0 or end_idx == len(s)-1:
                break
        
        # 以和右邻之间的分界线为中心
        if mid_idx == len(s)-1: # 最后一个元素，没有右邻，直接跳过
            continue
        count = 0
        while(True):
            start_idx = mid_idx - count
            end_idx = mid_idx + count + 1
            if s[start_idx] == s[end_idx]:
                count += 1
                if end_idx - start_idx + 1 > len(max_str):
                    max_str = s[start_idx:end_idx+1]
            else:
                break
            if start_idx == 0 or end_idx == len(s)-1:
                break      
        
    return max_str

if '__main__' == __name__:
    s_list = ["babad","cbbd"]
    for s in s_list:
        result = longestPalindrome4(s)
        print(f'{s}\t{result}')
                
    
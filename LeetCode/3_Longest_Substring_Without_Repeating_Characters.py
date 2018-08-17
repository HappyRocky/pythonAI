# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 09:28:48 2018

@author: gongyanshang1

最长无重复字字符串问题

Given a string, find the length of the longest substring without repeating characters.

给定一个字符串，找到最长的不包含重复字符的子字符串的长度。

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


def lengthOfLongestSubstring(s):
    '''
    动态规划。
    维护一个数存放最大长度。从左向右扫描，如果扫描到了重复字符，则比较现在的子字符串长度与最大长度的大小，然后将子字符串起始位置移到第一次出现此字符的后面，继续扫描。
    '''
    max_len = 0 # 存放最大长度
    start_idx = 0 # 子字符串的起始位置
    scaned_dict = dict() # 记录每次扫描到的字符，key=char,value=index
    for i in range(0, len(s)):
        
        # 如果字符存在于字典中，且位置是在起始位置的右边，说明遇到了重复字符
        if s[i] in scaned_dict and scaned_dict[s[i]] >= start_idx: 
            max_len = max(max_len, i - start_idx) # 统计重复字符之前的最长字符串
            start_idx = scaned_dict[s[i]] + 1 # 将起始位置修改为重复字符第一次出现的位置的右邻
            
        scaned_dict[s[i]] = i # 记录当前字符的位置
        
    return max_len

if '__main__' == __name__:
    s_list = ['abcabcbb','bbbbb','pwwkew']
    for s in s_list:
        print(f'输入{s},输出{lengthOfLongestSubstring(s)}')
        
        
        
        
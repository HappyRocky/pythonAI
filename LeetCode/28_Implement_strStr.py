# -*- coding: utf-8 -*-

'''
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

实现 strStr() 方法。
输入两个字符串 haystack, needle，返回在haystack中needle第一次出现的索引，如果从没有出现过，则返回-1。

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0
    if len(haystack)<len(needle):
        return -1
    
    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i+j] == needle[j]:
                if j == len(needle) - 1:
                    return i
            else:
                break
    return -1

if '__main__' == __name__:
    haystack = "hello"
    needle = "ll"
    print(strStr(haystack, needle))
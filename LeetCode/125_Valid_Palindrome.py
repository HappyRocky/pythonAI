# -*- coding: utf-8 -*-

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

给定一个字符串，判断是否是一个回文字符串。只需要考虑字母和数字，且忽略大小写。
备注：空字符串视为回文字符串。

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
"""
import re

def isPalindrome(s: str) -> bool:
    """
    维护左右两个指针，向中间靠拢，依次比较指向的字符，遇到非字母数字的便跳过，直至指针碰面。
    """
    if not s:
        return True
    i, j = 0, len(s) - 1
    pattern = re.compile(r'[a-zA-Z0-9]')
    while(i < j):
        if not pattern.match(s[i]):
            i += 1
            continue
        if not pattern.match(s[j]):
            j -= 1
            continue        
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

if '__main__' == __name__:
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))
    
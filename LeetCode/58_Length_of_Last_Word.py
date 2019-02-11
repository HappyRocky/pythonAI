# -*- coding: utf-8 -*-

'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.

给定一个字符串，包含大小写字母和空格。返回字符串中最后一个单词的长度。
如果最后一个单词不存在，返回0。
备注：
一个单词定义为不包含空格的字符序列。

Example:
Input: "Hello World"
Output: 5
'''

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    从后向前，寻找到第一个出现的非空格。
    然后继续向前，寻找到第一个出现的空格。
    两者之间的单词即为最后一个单词。
    """
    for i in range(len(s)-1, -1, -1):
        if s[i] != ' ':
            break
    else: # 都是空格
        return 0
    
    for j in range(i, -1, -1):
        if s[j] == ' ':
            break
    else: # i之前都是字母
        return i+1
    return i-j

if '__main__' == __name__:
    s = "Hello World"
    print(lengthOfLastWord(s))
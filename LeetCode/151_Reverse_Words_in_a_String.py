# -*- coding: utf-8 -*-

"""
Given an input string, reverse the string word by word.
Note:
A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.

给定一个输入字符串，将字符串以单词为单位进行反转。
备注：
一个单词指的是中间没有空格的字符序列。
输入字符串可能会包含前缀空格或者后缀空格。但是，反转后的字符串不能包含前缀空格或后缀空格。
你需要在反转后的字符串中将多个连续空格合并成单个空格。

Example 1:
Input: "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""
def reverseWords(s: str) -> str:
    """
    从前往后扫描一遍，根据空格识别单词
    """
    start = -1 # 一个单词的起始字符位置
    result = ''
    s = s + ' ' # 末尾追加空格，便于收集最后一个单词 
    for i in range(len(s)):
        if s[i] == ' ' and start != -1:
            if not result:
                result = s[start:i]
            else:
                result = s[start:i] + ' ' + result
            start = -1
        elif s[i] != ' ' and start == -1:
            start = i
    return result

if '__main__' == __name__:
    s = "the sky is blue"
    print(reverseWords(s))
    



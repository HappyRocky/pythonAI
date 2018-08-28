# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:36:38 2018

@author: gongyanshang1

Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.

Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.

实现一个字符串转整数的函数。
函数首先忽略掉一串空格，直到找到了第一个非空格字符。
然后，从这个字符开始，会有一个加号或者减号，随后跟着一串数字，将它们转为整数。
在这一串数字之后，字符串可能包含多余的字符，这些字符没有任何影响，需要忽略掉。
如果在字符串的开头非空格字符不是一个有效的整数字符，或者字符串为空，或者字符串仅仅包含空格字符，那么返回0.

备注：
只有空格字符' '可以称为空格字符。
假设我们的环境下整数只能储存在[−2^31,  2^31 − 1]范围内。如果整数超出了这个范围，那么返回 INT_MAX (^231 − 1) 或 INT_MIN (−2^31) 

示例：
Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

"""

def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """

    INT_MAX = 2**31-1
    INT_MIN = -2**31
    
    if len(str) == 0:
        return 0
    
    result = 0
    sign = 1 # 标志正负号
    has_first_char = False # 是否扫描到了第一个非空格字符
    for char in str:
        if not has_first_char: # 还没有扫描到第一个非空格字符
            if char == '+':
                sign = 1
                has_first_char = True
            elif char == '-':
                sign = -1
                has_first_char = True
            elif char >= '0' and char <= '9':
                has_first_char = True
                result = result * 10 + int(char)
            elif char == ' ':
                continue
            else:
                break
        else:
            if char >= '0' and char <= '9':
                result = result * 10 + int(char)
            else:
                break
    
    result = result * sign
    if result > INT_MAX:
        result = INT_MAX
    if result < INT_MIN:
        result = INT_MIN
    return result
        
if '__main__' == __name__:
    str = '-2147483648'
    print(myAtoi(str))

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 09:37:04 2018

@author: gongyanshang1

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

罗马数字可以由7个符号来表示： I, V, X, L, C, D 和 M.
符号          值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
比如，2的罗马数字为II，即两个1加起来。12的罗马数字为XII，即X+II。27的罗马数字为XXVII，即XX+V+II。
罗马数字的符号通常由大到小排列。但是，4的罗马数字并不是IIII，而是IV。因为1是在5前面，所以我们需要减去1。类似的例子有9，罗马数字为IX。一共有6种减法情况：
IV = 4
IX = 9
XL = 40
XC = 90
CD = 400
CM = 900
要求给定一个罗马数字，将其转为整数。整数的范围为 1 ~ 3999。

示例：
Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    从左向右扫描，扫描步长为1，扫描范围为2。要考虑到6个减法情况。    
    """
    
    romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    result = 0
    i = 0
    max_len = len(s)
    while(i < max_len):
        if s[i:i+2] in romans:
            result += romans[s[i:i+2]]
            i += 2
        else:
            result += romans[s[i]]
            i += 1
    return result
    

if '__main__' == __name__:
    num = 'MCMXCIV'
    print(romanToInt(num))
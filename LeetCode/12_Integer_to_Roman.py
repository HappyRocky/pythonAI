# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 09:08:22 2018

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
要求给定一个整数，将其转为罗马数字。整数的范围为 1 ~ 3999。

示例：
Example 1:
Input: 3
Output: "III"

Example 2:
Input: 4
Output: "IV"

Example 3:
Input: 9
Output: "IX"

Example 4:
Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.

Example 5:
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    
    罗马数字都是由大到小排列，因此按照从大到小的顺序扫描，只要比扫描到的数字大，就把这个数字的罗马符号写下来。
    """
    
    romans = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
    result = ''
    while(num > 0):
        for i in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            if num >= i:
                result += romans[i]
                num -= i
                break
    return result

def intToRoman2(num):
    """
    :type num: int
    :rtype: str
    
    改进版。
    不必每次都比较一遍大小，而是利用除法结果，一次性将某个罗马符号全部写全，接下来再写下一个罗马符号。
    """
    
    dict = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ""
    for letter, n in zip(dict, nums):
        result += letter * int(num / n)
        num %= n
    return result

if '__main__' == __name__:
    num = 1994
    print(intToRoman2(num))

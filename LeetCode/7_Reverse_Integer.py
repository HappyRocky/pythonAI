# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:22:45 2018

@author: gongyanshang1

Given a 32-bit signed integer, reverse digits of an integer.
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

给定一个32位的有符号整数，将其所有数字反转。
备注：
假设只处理[−2^31,  2^31 − 1]范围内的整数。当反转后的结果溢出时，返回0.

示例：
Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

"""

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    
    result = 0
    a = abs(x)
    while(a != 0):
        pop = a % 10
        a = (a - pop) / 10
        result = result * 10 + pop
    if x > 0 and result < 2**31:
        return int(result)
    if x < 0 and result <= 2**31:
        return -int(result)
    return 0

if '__main__' == __name__:
    x = -2147483648
    print(reverse(x))
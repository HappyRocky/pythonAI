#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.

给定两个整数，代表一个分式的分子和分母。
返回分式的字符串格式。
如果小数部分是无穷循环的，将重复部分用括号括起来。

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""

def fractionToDecimal(numerator: int, denominator: int) -> str:
    """
    实现除法。
    """
    if numerator == 0:
        return '0'
    # 记录正负号
    flag = '-' if numerator * denominator < 0 else ''
    numerator = abs(numerator)
    denominator = abs(numerator)


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
    denominator = abs(denominator)

    # 是否可以整除
    result_list = [str(numerator // denominator)]
    reminder = numerator % denominator
    if reminder == 0:  # 可以整除
        return flag + ''.join(result_list)

    # 不可以整除，开始循环
    result_list.append('.')
    result_map = {}  # 存放每一位的位置，便于发现循环起始点

    while reminder != 0:

        # 结果之前曾经出现过，说明进入了循环
        if reminder in result_map:
            result_list.insert(result_map[reminder], '(')
            result_list.append(')')
            return flag + ''.join(result_list)

        result_map[reminder] = len(result_list)  # 记录所在位置
        reminder *= 10  # 借位
        result = str(reminder // denominator)
        reminder = reminder % denominator
        result_list.append(result)

    return flag + ''.join(result_list)


if '__main__' == __name__:
    numerator = 1
    denominator = 33
    print(fractionToDecimal(numerator, denominator))

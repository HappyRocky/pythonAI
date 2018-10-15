# -*- coding: utf-8 -*-

'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 2^31 − 1 when the division result overflows.

给定两个整数，作为除数和被除数，计算除法结果，不能使用乘法、除法和取模运算。

备注：
两个整数都是32位有符号整数。
除数不会为0。
假设我们的环境只能处理范围为[−2^31,  2^31 − 1]的整数。如果除法结果溢出，则返回2^31 − 1。


Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

'''

def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    统计有多少个除数相加可以刚好超过被除数。
    """
    if dividend == 0:
        return 0
    
    #是否是正数
    is_positive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
    
    dividend = abs(dividend)
    divisor = abs(divisor)
    result = 0 # 除数的个数
    sum = 0 # 除数累加结果
    while(sum <= dividend):
        sum += divisor
        result += 1
    result -= 1
    if not is_positive:
        result = -result
    if result < -2**31 or result > 2**31 - 1:
        result = 2**31 - 1
    return result

def divide2(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    改进版。
    每次并不是只加一个除数，而是可以一次性加上n个除数，减少时间复杂度。
    当然，前提是需要知道这n个除数之和，这个可以从前面的结果直接得到。
    """
    if dividend == 0:
        return 0
    
    #是否是正数
    is_positive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
    
    dividend = abs(dividend)
    divisor = abs(divisor)
    result = 0 # 除数的个数
    sum = 0 # 除数累加结果
    sum_list = [(1, divisor)] # 存放二元元组，第一位为一个正整数n，第二位为n个除数之和。
    while(True):
        have_pop = False
        while sum_list and sum + sum_list[-1][1] > dividend: # 优先累加最大的数，如果超过被除数，则改为较小数
            sum_list.pop()
            have_pop = True
        if not sum_list: # 所有可用加数都会溢出，则说明距离被除数的差已经不足一个除数了
            break
        sum += sum_list[-1][1]
        result += sum_list[-1][0]
        if not have_pop:
            sum_list.append((sum_list[-1][0]<<1, sum_list[-1][1]<<1))
    if not is_positive:
        result = -result
    if result < -2**31 or result > 2**31 - 1:
        result = 2**31 - 1
    return result
    
if '__main__' == __name__:
    dividend = 2147483647
    divisor = 1
    print(divide2(dividend, divisor))
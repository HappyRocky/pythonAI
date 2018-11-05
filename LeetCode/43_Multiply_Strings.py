# -*- coding: utf-8 -*-

'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

给定两个非负整数字符串 num1 和 num2，返回两个数的乘积字符串。

备注：
两个整数字符串的长度都 < 110。
两个数都只包含数字 0-9。
两个数都不1️0开头，除非整个字符串就是0.
不能使用任何内置的大整数库，不能将输入字符串直接转为整数。

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

'''

def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    使用乘法的手算规则，从低位到高位依次相乘。
    num1 = 'abcd'
    num2 = 'efg'
    
        a  b  c  d
        *  e  f  g
        -----------
        ag bg cg dg 
     af bf cf df
  ae be ce de
  -----------------
    """
    
    if num1 == '0' or num2 == '0':
        return '0'
    
    def submultiply(large, single):
        '''
        一个字符串和单一字符相乘
        返回一个字符数组，低位在前。
        '''
        if single == '0':
            return ['0']
        single = int(single)
        result = []
        l = len(large)
        carry = 0 # 向前进位
        for i in range(l):
            char = large[l-1-i] # 倒序取出
            num = int(char)
            mul = num * single + carry # 相乘并加上进位
            carry = mul // 10
            mul -= 10 * carry
            result.append('%d' % mul)
        if carry > 0: # 最高位乘完之后还有进位
            result.append('%d' % carry)
        return result
    
    # num2的每一位与num1相乘，结果放入 mul_list
    mul_list = [] 
    for i in range(len(num2)):
        single = num2[-1-i]
        mul = ['0'] * i + submultiply(num1, single)
        mul_list.append(mul)
    
    # 所有 mul_list 相加
    result_list = []
    carry = 0 # 进位
    for i in range(len(mul_list[-1])): # 最长数组的位数
        total = carry # 所有 result_list 第 i 位相加
        for string in mul_list:
            if len(string) <= i: # 略过长度不够的数组
                continue
            total += int(string[i])
        carry = total // 10
        total -= 10 * carry
        result_list.append('%d' % total)
    if carry > 0:
        result_list.append('%d' % carry)
    
    return ''.join(result_list)[::-1]

if '__main__' == __name__:
    num1 = ['1'] * 100
    num2 = ['2'] * 100
    print(multiply(num1, num2))
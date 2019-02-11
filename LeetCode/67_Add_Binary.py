# -*- coding: utf-8 -*-

'''
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

给定两个二进制字符串，返回他们的和（也是一个二进制字符串）
输入的字符串都是非空的，并且只包含1或0。

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    按照手算加法的步骤，从最低位开始，同位相加，并考虑是否有进位。
    """
    # 保证a的长度小于等于b的长度
    if len(a) > len(b):
        a,b = b,a 
        
    # 从最低位开始加起
    la, lb = len(a), len(b)
    a = '0' * (lb-la) + a # 两个字符串长度相同，高位补0
    add_one = 0 # 进位
    result = ''
    for i in range(lb-1, -1, -1):
        s = int(a[i]) + int(b[i]) + add_one
        add_one, s = divmod(s, 2)
        result += str(s)
    if add_one == 1:
        result += '1'
    return result[::-1]

if '__main__' == __name__:
    a = "1010"
    b = "1011"
    print(addBinary(a, b))
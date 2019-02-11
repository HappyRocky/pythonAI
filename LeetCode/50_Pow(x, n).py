# -*- coding: utf-8 -*-

'''
Implement pow(x, n), which calculates x raised to the power n (x^n).
Note:
1、-100.0 < x < 100.0
2、n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]

实现函数 pow(x,n)，返回 x^n。
备注：
1、-100.0 < x < 100.0
2、n是一个32位的整数，范围为[−2^31, 2^31 − 1]

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000

'''

def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    利用 x^n = (x^(n/2))^2，使用分治法。
    """
    def fun(x, n):
        '''
        递归，x^n = (x^(n/2))^2
        '''
        # 递归结束条件
        if n == 1:
            return x
        # 递归
        half = fun(x, n // 2)
        if n % 2 == 1: # 如果是奇数，则还需要再乘以一个x
            return half * half * x
        else:
            return half * half
        
    if n == 0:
        return 1
    elif n > 0:
        return fun(x, n)
    else:
        return 1/fun(x, -n)

if '__main__' == __name__:
    x, n = 2.10000, 3
    print(myPow(x, n))
    
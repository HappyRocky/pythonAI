# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:30:15 2018

@author: gongyanshang1

斐波那契数列的三种实现：递归、尾递归、循环
斐波那契数列：1,1,2,3,5,8,...
"""

def fibonacci(n):
    '''
    普通递归
    '''
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_tail(n, ret1, ret2):
    '''
    尾递归
    '''
    if n == 0:
        return ret1
    return fibonacci_tail(n-1, ret2, ret1 + ret2)

def fibonacci_cycle(n):
    '''
    循环实现
    '''
    result = 0
    if n == 0 or n == 1:
        return n
    
    f0 = 0
    f1 = 1
    for i in range(0, n-1):
        result = f0 + f1
        f0 = f1
        f1 = result
    return result

if '__main__' == __name__:
    n = 3
    print(fibonacci(n))
    print(fibonacci_tail(n, 0, 1))
    print(fibonacci_cycle(n))


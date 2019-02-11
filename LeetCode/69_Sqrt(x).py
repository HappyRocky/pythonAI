# -*- coding: utf-8 -*-

'''
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

完成函数 int sqrt(int x)。
计算并返回 x 的平方根，其中 x 是一个非负整数。
返回结果去掉小数，只保留整数。

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
'''

def mySqrt(x):
    """
    :type x: int
    :rtype: int
    枚举法
    """
    if x <= 1:
        return x
    for i in range(x+1):
        if i * i > x:
            break
    return i-1

def mySqrt2(x):
    """
    :type x: int
    :rtype: int
    牛顿逼近法.
    百度百科：https://baike.baidu.com/item/%E7%89%9B%E9%A1%BF%E9%80%BC%E8%BF%91%E6%B3%95/1516472?fr=aladdin
    寻找 f(y)=0 的解的迭代公式： y := y - f(y)/f'(y)
    应用到本题，则 f(y) = y^2 - x，求使得 f(y) = 0 的 y 值。
    其中，f'(y) = 2y，因此迭代公式为 y := y - (y^2-x)/(2y) = y/2 + x / (2y)
    """
    y = x
    while (y*y - x) > 0.1:
        y = y/2 + x / (2*y)
        print(y)
    y = int(y)
    if (y+1)**2 < x: # 可能y=3.9999但是真实结果为4.0001，因此需要判断最后结果是 y 还是 y+1。
        return y+1
    else:
        return y
    
def mySqrt3(x):
    '''
    二分查找法
    '''
    if x <= 1:
        return x
    def binary_search(x, l, u):
        '''
        递归查找x的开方值。
        '''
        if u - l <= 1:
            return l
        mid = (u+l)//2
        if mid**2 == x:
            return mid
        elif mid**2 > x:
            return binary_search(x, l, mid)
        else:
            return binary_search(x, mid, u)
    return binary_search(x, 0, x)
    
if '__main__' == __name__:
    x = 9
    print(mySqrt3(x))
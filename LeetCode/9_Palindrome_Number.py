# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 09:12:54 2018

@author: gongyanshang1

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

判断一个整数是否是一个回文数（后往前读与从前往后读一样）

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    
    def fun_rec(x, length):
        '''
        递归函数，判断x是否是回文数
        length:x的长度
        '''
        
        # 递归结束条件
        if length <= 1:
            return True
        
        # 比较最低位和最高位
        low = x % 10
        up = int(x / (10 ** (length - 1)))
        if low == up:
            x = int((x - low - up * (10 ** (length - 1))) / 10)
            return fun_rec(x, length - 2)
        return False
    
    # 边界条件
    if x < 0:
        return False
    
    # 判断x的长度
    length = 1
    while(x / (10 ** length) >= 1):
        length += 1
        
    return fun_rec(x, length)


def isPalindrome2(x):
    """
    :type x: int
    :rtype: bool
    对x反转一半，然后与另一半对比是否相等
    """
    
    if x < 0 or (x > 0 and x % 10 == 0):
        return False
    
    revert = 0
    while(x > revert):
        revert = revert * 10 + x % 10
        x = int(x / 10)
    
    return x == revert or x == int(revert / 10)
    
if '__main__' == __name__:
    x = 1001
    print(isPalindrome(x))
    print(isPalindrome2(x))
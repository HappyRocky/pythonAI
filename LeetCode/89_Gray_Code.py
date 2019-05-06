# -*- coding: utf-8 -*-
"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

格雷编码是一个二进制数字系统，其中两个相邻的编码只有一位是不同的。
给定一个非负整数n，代表了编码的位数，打印出格雷编码的序列。格雷编码的序列肯定从0开始。

Example 1:
Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2
For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1

Example 2:
Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
"""


import math
def grayCode(n: int) -> list:
    """
    利用二进制格雷编码的镜像规则，递归实现：
    n+1位格雷码的集合 = n位格雷码集合(顺序)加前缀0 + n位格雷码集合(逆序)加前缀1
    这个规则用整数表现出来：前缀加0值不变，前缀加1则相当于加上2的(n-1)次方
    """
    # 递归结束条件
    if n == 1:
        return [0, 1]
    # 开始递归
    l = grayCode(n-1)
    return l + [x + int(math.pow(2, n-1)) for x in l[::-1]]

def grayCode2(n: int) -> list:
    """
    整数转格雷编码。
    规则：
    1、n右移一位，高位补0，得到m
    2、n和m异或
    """
    result = []
    for i in range(1 << n): # n 位，则共有 2 的 n 次方个编码，即 1 << n
        result.append((i >> 1) ^ i)
    return result

if '__main__' == __name__:
    n = 3
    print(grayCode2(n))
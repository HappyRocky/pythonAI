# -*- coding: utf-8 -*-

'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

你正在爬楼梯，共有 n 层台阶。
每次可以爬 1 层或 2 层。
问有多少种不重复的方法可以从楼梯底爬到楼梯顶。

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    爬n层台阶，可以分解为：
    1、第一步爬1层，然后继续爬剩下的n-1层
    2、第一步爬2层，然后继续爬剩下的n-2层
    这两种方法是互斥且完备的。
    因此，climbStairs(n) = climbStairs(n-1) + climbStairs(n-2)
    即斐波那契数列。
    """
    a, b = 1, 1
    for i in range(n):
        a, b = b, a+b
    return a

if '__main__' == __name__:
    n = 3
    print(climbStairs(n))
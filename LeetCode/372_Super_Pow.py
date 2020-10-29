# -*- coding: utf-8 -*-
"""
你的任务是计算 a^b 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
输入: a = 2, b = [3]
输出: 8
"""

class Solution:
    def mypow(self, m, k):
        """
        求 m^k 并对 1337 取模
        利用：
        (a * b) % k = ((a % k) * (b % k)) % k
        """
        res = 1
        for _ in range(k):
            res *= m
            res %= 1337
        return res

    def superPow(self, a: int, b: list) -> int:
        """
        递归，利用：
        a ^ [1,2,3] = a^3 * (a^[1,2])^10
        """
        if not b or a == 1:
            return 1
        a %= 1337
        s1 = self.mypow(a, b[-1])
        s2 = self.mypow(self.superPow(a, b[:-1]), 10)
        return s1 * s2


if '__main__' == __name__:
    a = 2
    b = [3]
    print(Solution().superPow(a, b))




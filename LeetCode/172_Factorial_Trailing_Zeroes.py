# -*- coding: utf-8 -*-

"""
Given an integer n, return the number of trailing zeroes in n!.

给定一个整数n，返回 n! 尾数中 0 的数量。

Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        看因子里面有多少个2*5，就有多少个0
        进一步，由于2的数量总是比5多，所以只需要看有多少个5即可。
        result = n / 5 + n / 25 + n / 125 + ...
        :param n:
        :return:
        """
        result = 0
        while n > 0:
            result += n // 5
            n //= 5
        return result


if '__main__' == __name__:
    print(Solution().trailingZeroes(10))

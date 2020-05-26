# -*- coding: utf-8 -*-

"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

给定一个正数，返回其在excel表中对应的列名。

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:
Input: 1
Output: "A"

Example 2:
Input: 28
Output: "AB"

Example 3:
Input: 701
Output: "ZY"

"""

class Solution:
    def convertToTitle(self, n: int) -> str:
        """
        将十进制改为26进制
        :param n: 正数
        :return: 字符串
        """
        map_list = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        result = ''
        while n > 0:
            m = n % 26
            n = n // 26
            if m == 0:
                m = 26
                n -= 1
            result = map_list[m] + result
        return result

if '__main__' == __name__:
    solution = Solution()
    n = 701
    print(solution.convertToTitle(n))

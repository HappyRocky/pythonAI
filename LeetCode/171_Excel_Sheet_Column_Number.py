# -*- coding: utf-8 -*-
"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

给定一个Excel中的列名称，返回对应的列序号。

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
"""

class Solution:
    def titleToNumber(self, s: str) -> int:
        map_dict = {'A': 1,
                    'B': 2,
                    'C': 3,
                    'D': 4,
                    'E': 5,
                    'F': 6,
                    'G': 7,
                    'H': 8,
                    'I': 9,
                    'J': 10,
                    'K': 11,
                    'L': 12,
                    'M': 13,
                    'N': 14,
                    'O': 15,
                    'P': 16,
                    'Q': 17,
                    'R': 18,
                    'S': 19,
                    'T': 20,
                    'U': 21,
                    'V': 22,
                    'W': 23,
                    'X': 24,
                    'Y': 25,
                    'Z': 26
                    }
        result = 0
        jinzhi = 1
        for i in range(1, len(s) + 1):
            result += map_dict[s[-i]] * jinzhi
            jinzhi *= 26
        return result


if '__main__' == __name__:
    s = 'ZY'
    print(Solution().titleToNumber(s))
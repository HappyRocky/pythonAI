# -*- coding: utf-8 -*-

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

给定一个非空整数序列，除了某个元素，其他每个元素都出现了两次。找到这个单独的元素。
备注：
算法应该有一个线性的时间复杂度，且不需要额外的空间。

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""

def singleNumber(nums: list) -> int:
    """
    维护一个set，每次遍历到一个元素，查看set中是否含有这个元素。
    如果有，则将此元素从set中消除，否则加入到set。
    最后set中剩下的那个元素即为所求。
    """
    s = set()
    for n in nums:
        if n in s:
            s.remove(n)
        else:
            s.add(n)
    return list(s)[0]

def singleNumber2(nums: list) -> int:
    """
    使用异或的交换律和结合律：
    a^b^c^a^c = (a^a)^(c^c)^b = b
    所以将所有元素依次进行异或，最后的结果即为单独的那个元素。
    """
    result = 0
    for n in nums:
        result ^= n
    return result

    # 一句话：
    # from functools import reduce
    # return reduce(lambda x,y:x^y, nums)

if '__main__' == __name__:
    nums = [4,1,2,1,2]
    print(singleNumber2(nums))

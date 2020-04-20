# -*- coding: utf-8 -*-

"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

给定一个非空整数序列，除了某个元素，其他每个元素都出现了3次。找到这个单独的元素。
备注：
算法应该有一个线性的时间复杂度，且不需要额外的空间。

Example 1:
Input: [2,2,3,2]
Output: 3

Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99
"""

def singleNumber(nums: list) -> int:
    """
    与上一题一样，同样使用异或的交换律和结合律。
    不过，这次最多出现3次，所以不能只维护一个数值，需要两个，记为 ones 和 twos，均初始化为0。
    假设我们需要让这两个数呈现这样的状态：
    当两个数和某个数a进行第一次异或后，ones 等于 a， twos 等于 0。
    当两个数和某个数a进行第二次异或后，ones 等于 0， twos 等于 a。
    当两个数和某个数a进行第三次异或后，ones 等于 0， twos 等于 0。
    然后在扫描一遍之后，出现三次的数的异或结果都是0，而出现一次的数的异或结果是 ones。因此最后返回 ones 即可。
    """
    ones, twos = 0, 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones

# 扩展：除了某个数只出现了1次，其他数都出现了5次。求single num。
def single(nums: list) -> int:
    """
    5个状态需要3个变量才行（ones, twos, threes），可以这样规划：
    出现0次，三个变量为  000
    出现一次，三个变量为 100
    出现两次，三个变量为 010
    出现三次，三个变量为 110
    出现四次，三个变量为 001
    出现五次，三个变量为 000
    可以发现规律：
    1、当上一次 ones = 0 时，这一次 twos 就与上一次相同，否则直接异或。
    2、当上一次 threes = 1 时，这一次 ones = 0，否则直接异或。
    3、当这一次 ones 和 twos 都是 0 时，这一次 threes 直接异或，否则 threes = 0。
    备注：与上一次相同相当于异或0。
    """
    ones, twos, threes = 0, 0, 0
    for num in nums:
        twos = twos ^ (num & ones)
        ones = (ones ^ num) & ~threes
        threes = (threes ^ num & ~ones & ~twos)
    return ones

if '__main__' == __name__:
    nums = [2,2,3,2,2,2]
    print(single(nums))
    
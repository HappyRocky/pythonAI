# -*- coding: utf-8 -*-
'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

给定一个非空数字序列，表示一个非负整数。
要求将这个整数加1。
序列中每个元素都是一个单独的数字，且最高位是数组的第一个元素。
可以假设最高位不是0，除非就是整个序列就只有一个0。

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    按照手写加法的定义，从最低位开始加1，并计算每一位是否满10需要进1。
    """
    need_add = 1 # 是否需要加1
    for i in range(len(digits)-1, -1, -1):
        if need_add == 0: # 没有进位，则加法结束
            break
        digits[i] += need_add
        need_add, digits[i] = divmod(digits[i], 10)
    if need_add == 1:
        digits = [1] + digits
    return digits

if '__main__' == __name__:
    digits = [9,9,9,9]
    print(plusOne(digits))
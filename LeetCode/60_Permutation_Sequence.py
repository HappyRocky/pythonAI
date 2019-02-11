# -*- coding: utf-8 -*-

'''
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

集合 [1,2,3,...,n] 共有 n! 个唯一的排列。
将所有排列方法按照顺序排序，可以得到以下序列：n=3时有
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回序列中第 k 个排列。

备注：
n 的范围为 1~9
k 的范围为 1~9!

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"
'''

def getPermutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    分治法。
    从一共 n! 种排列中，选出第 k 个排列。
    这些排列是有规律的：前 (n-1)! 个排列的第1个字符肯定是这 n 个数中的最小值，也就是 1。
    比如 [1,2,3,4] 这 4 个数共有 4! 中排列，他们的前 3! 种排列的第1个字符肯定是 1，接下来的 3! 种排列的第1个字符肯定是2 ... 直到最后一组 3! 种排列的第1个字符肯定是 4。
    一共有 4 组 3! 种排列，即总排列数共有 4*3! = 4! 种。
    因此，可以使用分治法，先确定第1个字符，然后递归决定剩下的字符。
    """
    # 存储阶乘
    factorial_list = [1]
    for i in range(1, n+1):
        factorial_list.append(factorial_list[-1] * i)
    
    def func(digits, k):
        '''
        找到数组digits的第k个排列
        '''
        n = len(digits)
        if n == 1: # 递归结束条件
            return str(digits[0])
        first_idx, next_k = divmod(k, factorial_list[n-1])
        first = digits.pop(first_idx)
        return str(first) + func(digits, next_k)
    
    return func(list(range(1, n+1)), k-1)

if '__main__' == __name__:
    n = 3
    k = 3
    print(getPermutation(n, k))

# -*- coding: utf-8 -*-

"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

给定n，求所有不重复的二叉搜索树(元素为1...n)的数量

Example:
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

   
def numTrees(n: int, memo=dict()) -> int:
    """
    递归，从待选列表中选出一个数，作为根节点，所有小于此数的作为左树，大于此数的作为右树。
    """
    if n in memo:
        return memo[n]
    result = 0 if n == 0 else sum([max(numTrees(i), 1) * max(numTrees(n-i-1), 1) for i in range(n)])
    memo[n] = result
    return result
    

if '__main__' == __name__:
    n = 19
    result = numTrees(n)
    print(result)
            
        
# -*- coding: utf-8 -*-

'''
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

给定一个字符串 s1，我们可以将它表示成一个二叉树，方法是递归地将其划分为两个非空的子串。

Below is one possible representation of s1 = "great":

以下是对 s1='great'的一种表达方法：
    
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
          
To scramble the string, we may choose any non-leaf node and swap its two children.

为了打乱字符串，我们可以选择任意一个非叶子节点，交换他的两个子节点。

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

比如，如果我们选择节点"gr"并交换他的子节点，则他会产生一个乱序字符串"rgeat"。

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".
Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

我们称"rgeat"是"great"的一个乱序字符串。
同样地，如果我们继续交换"eat"和"at"的子节点，就可以得到乱序字符串"rgtae"。

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".
Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

我们称"rgtae"是"great"的一个乱序字符串。

给定两个同样长度的字符串 s1 和 s2，判断 s2 是否是 s1 的乱序字符串。

Example 1:
Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:
Input: s1 = "abcde", s2 = "caebd"
Output: false
'''

def isScramble(s1: str, s2: str) -> bool:
    '''
    使用递归，将s1的所有乱序字符串都列举出来，看是否包含s2.
    缺点：时间复杂度很大。T(n) = T(1)*T(n-1)*2 + T(2)*T(n-2)*2 + ... + T(n-1)*T(1)*2
    '''
    def get_scrambled(s):
        '''
        递归得到s的所有乱序字符串。
        '''
        n = len(s)
        if n <= 1:
            return [s]
        result_list = []
        for i in range(1, n): # 两部分：s[:i] 和 s[i:]
            group1 = get_scrambled(s[:i])
            group2 = get_scrambled(s[i:])
            # [:i] 和 s[i:] 的所有乱序字符串进行笛卡尔积，并且有前后之分
            for s1 in group1:
                for s2 in group2:
                    result_list.append(s1+s2)
                    result_list.append(s2+s1)
        return result_list
    return s2 in get_scrambled(s1)

def isScramble2(s1: str, s2: str) -> bool:
    """
    s1 与 s2 互为乱序字符串 <=> 存在一种分割，将 s1 和 s2 分别分割为两部分，两部分的大小分别对应相等，且两部分分别互为乱序字符串。
    """
    def fun(s1:str, s2:str, memo_dict:dict):
        """
        递归，判断 s1 和 s2 是否互为乱序字符串。
        """
        # 递归边界条件
        if len(s1) != len(s2):
            return False
        if len(s1) <= 1:
            return s1 == s2
        if (s1, s2) in memo_dict or (s2, s1) in memo_dict:
            return memo_dict.get((s1, s2), False) or memo_dict.get((s2, s1), False)
        # 寻找一种分割，使得两部分分别互为乱序字符串
        for i in range(1, len(s1)):
            if (fun(s1[:i], s2[:i], memo_dict) and fun(s1[i:], s2[i:], memo_dict)) or\
            (fun(s1[:i], s2[-i:], memo_dict) and fun(s1[i:], s2[:-i], memo_dict)):
                memo_dict[(s1, s2)] = True
                memo_dict[(s2, s1)] = True
                return True
        memo_dict[(s1, s2)] = False
        memo_dict[(s2, s1)] = False
        return False
    return fun(s1, s2, {})



if '__main__' == __name__:
    s1 = "great"
    s2 = "rgeat"
    print(isScramble2(s1, s2))
            
# -*- coding: utf-8 -*-

'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

给定两个整数 n 和 k，要求从1~n中选出k个数，返回所有可能的组合。

Example:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    从数学来看，共有C_n^k种组合。
    从编程来看，可以使用深度优先方法进行遍历。
    要求从n个数中选择k个，可以先在里面选择1个，然后在剩下的n-1个数中递归选择k-1个。
    """
    def select(result_list, pre_list, remain_list, k):
        '''
        从列表remain_list中选择k个数，与pre_list拼接到一起，追加到结果列表中
        '''
        # 递归结束条件
        if k == 0:
            result_list.append(pre_list)
            return
        if len(remain_list) == k:
            result_list.append(pre_list + remain_list)
            return
        if len(remain_list) < k:
            return
        # 从剩余列表欧中依次挑选1个，然后在这个数字之后的列表中选择剩余的k-1个，防止重复
        for i in range(len(remain_list)-k+1):
            select(result_list, pre_list+[remain_list[i]], remain_list[i+1:], k-1)
    result_list = []
    select(result_list, [], list(range(1, n+1)), k)
    return result_list

if '__main__' == __name__:
    n = 4
    k = 2
    print(combine(n, k))
    
        
    
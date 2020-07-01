# -*- coding: utf-8 -*-
'''
01背包问题
有N件物品和一个容量为V的背包。第i件物品的重量是w[i]，价值是v[i]。求解将哪些物品装入背包可使这些物品的重量总和不超过背包容量，且价值总和最大
'''

def bag01(N, V, w, v):
    '''
    动态规划
    状态：当前背包的剩余容量、尚未加入到背包中的物品
    选择：选择其中一个放入背包，或者所有物品都不能放入背包
    dp(m, n)：将前m件物品放入到容量为n的背包中，返回最大的价值总和
    :param N:物品数
    :param V:容量
    :param w:重量列表
    :param v:价值列表
    :return:列表
    '''
    memo_dict = dict()
    def dp(m, n):
        if m == 0 or n <= 0:
            return 0
        if (m, n) in memo_dict:
            return memo_dict[(m, n)]
        res = max(dp(m-1, n), dp(m-1, n-w[m-1]) + v[m-1])
        memo_dict[(m, n)] = res
        return res
    return dp(N, V)


if '__main__' == __name__:
    N = 3
    V = 4
    w = [2, 1, 3]
    v = [4, 2, 3]
    print(bag01(N, V, w, v))
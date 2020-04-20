# -*- coding: utf-8 -*-

"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

给定一个序列，第i个元素是第i天的股票价格。
你只允许最多交易一次（即，完成一次买股票和卖股票），设计一个算法，来找到最大利润。
在卖股票前必须要买股票。

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
             
Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

def maxProfit(prices: list) -> int:
    """
    动态规划。
    前i天的最大利润，有两种可能，一种是在前i-1天就完成了买和卖，一种是在前i-1天买，在第i天卖。取这两种方法的较大利润。
    维护一维向量dp，dp[i] 表示前i天的最大利润，则：
    dp[i] = max(dp[i-1],  第i天价格 - 前i-1天最低价格)
    """
    # 无法买卖
    m = len(prices)
    if m <= 1:
        return 0
    # 初始化
    dp = [0] * m # dp[i]为前i天的最大利润，i从0开始
    min_list = [0] * m # min_list[i]为前i天的最低价格
    min_list[0] = prices[0] # 第0天，只有最低价格，没有利润
    for i in range(1, m):
        dp[i] = max(dp[i-1], prices[i] - min_list[i-1])
        min_list[i] = min(prices[i], min_list[i-1])
    return dp[m-1]

if '__main__' == __name__:
    prices = [7,6,4,3,1]
    print(maxProfit(prices))
    
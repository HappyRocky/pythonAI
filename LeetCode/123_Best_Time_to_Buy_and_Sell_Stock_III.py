# -*- coding: utf-8 -*-

"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

给定一个序列，第i个元素是第i天的股票价格。
设计一个算法，找到最大利润。可以进行最多两次交易。
备注：不能同时进行多次交易，即当再次买股票之前一定要卖掉已有股票。

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

def maxProfit(prices: list) -> int:
    """
    动态规划。
    维护4个变量：cost1, profit1, cost2, profit2
    分别表示第一次和第二次交易的最小买入代价和最大卖出利润，最后profit2为所求。
    以 [3,3,5,0,0,3,1,4] 为例，结果为 6 = (3-0)+(4-1) = 4-(1-(3-0))。
    其中，0是cost1，(3-0)是profit1，(1-(3-0))是cost2，4-(1-(3-0))是profit2.
    """
    cost1, cost2, profit1, profit2 = float('inf'), float('inf'), 0, 0
    for price in prices:
        cost1 = min(cost1, price)
        profit1 = max(profit1, price - cost1)
        cost2 = min(cost2, price - profit1)
        profit2 = max(profit2, price - cost2)
    return profit2

if '__main__' == __name__:
    prices = [3]
    print(maxProfit(prices))
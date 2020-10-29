# -*- coding: utf-8 -*-

"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

给定一个序列，第i个元素是第i天的股票价格。
设计一个算法，找到最大利润。可以进行多次交易，即可以多次买卖。
备注：不能同时进行多次交易，即当买股票之前一定要卖掉已有股票。

Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
             
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
    只要遇到 prices[i] > prices[i+1] 的情况，便考虑进行一次买卖，在i之前买，在i当天卖。
    """
    prices.append(0) # 追加一天，价格为0，便于在最后一天让算法卖出股票
    m = len(prices)
    if m <= 2:
        return 0
    result = 0
    min_price = prices[0] # 当前交易阶段的历史最小价格
    for i in range(1, m):
        if prices[i] < prices[i-1]: # 价格变低，说明在昨天是高点，可以卖出，而且选择之前历史最低点买入
            result += prices[i-1] - min_price
            min_price = prices[i]
    return result

def maxProfit2(prices: list) -> int:
    """
    只要遇到 prices[i] > prices[i-1] 的情况，便考虑进行一次买卖，在i-1买入，在i卖出。
    """
    result = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            result += prices[i] - prices[i-1]
    return result

if '__main__' == __name__:
    prices = [1,2,3,4,5]
    print(maxProfit2(prices))
    
    
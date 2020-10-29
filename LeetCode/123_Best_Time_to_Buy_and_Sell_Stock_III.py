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

def maxProfit2(prices: list) -> int:
    """
    递归，深度优先遍历
    此过程的状态可以用3个变量来表示：
    index：表示是哪一天
    status：表示当前状态是买入还是卖出，0是卖出，1是买入
    k：表示已经交易了几次
    状态之间的转移可以用3个行动表示：
    不动、买、卖
    缺点是时间复杂度高，本质上是把所有可能性都遍历了一遍。
    """
    memo = dict()
    def dfs(index, status, k):
        """
        深度优先遍历
        表示从当前状态开始，在接下来的所有天内，能够获得的最大利润
        """
        # 递归停止条件，已经到了最后一天，或者完成了2次交易
        if index == len(prices) or k >= 2:
            return 0
        if (index, status, k) in memo:
            return memo[(index, status, k)]
        # 无论是买入还是卖出状态，都可以选择"不动"
        a = dfs(index + 1, status, k)
        # 如果是买入状态，则还可以选择卖出
        if status == 1:
            b = dfs(index + 1, 0, k + 1) + prices[index]
        else:  # 如果是卖出状态，则还可以选择买入
            b = dfs(index + 1, 1, k) - prices[index]
        result = max(a, b)
        memo[(index, status, k)] = result
        return result
    return dfs(0, 0, 0)




if '__main__' == __name__:
    prices = [3,3,5,0,0,3,1,4]
    print(maxProfit2(prices))
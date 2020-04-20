# -*- coding: utf-8 -*-

"""
给定一个序列，第i个元素是第i天的股票价格。
设计一个算法，找到最大利润。可以进行最多n次交易。
备注：不能同时进行多次交易，即当再次买股票之前一定要卖掉已有股票。
"""

def max_frofit(prices, n):
    """
    动态规划。
    以n=2为例，即最多可以进行2次交易：
    维护4个变量：cost1, profit1, cost2, profit2
    分别表示第一次和第二次交易的最小买入代价和最大卖出利润
    以 [3,3,5,0,0,3,1,4] 为例，结果为 6 = (3-0)+(4-1) = 4-(1-(3-0))。
    其中，0是cost1，(3-0)是profit1，(1-(3-0))是cost2，4-(1-(3-0))是profit2.
    最后profit2为所求。
    当n为其他值时同理。
    """
    cost_list = [float('inf')] * n
    profit_list = [0] * n
    for price in prices:
        for i in range(n):
            cost_list[i] = min(cost_list[i], price - (profit_list[i-1] if i > 0 else 0))
            profit_list[i] = max(profit_list[i], price - cost_list[i])
    return profit_list[-1]

if '__main__' == __name__:
    prices = [3,3,5,0,0,3,1,4]
    n = 8
    print(max_frofit(prices, n))
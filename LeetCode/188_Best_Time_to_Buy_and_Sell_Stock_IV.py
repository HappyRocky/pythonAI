# -*- coding: utf-8 -*-
"""
Say you have an array for which the i-th element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.
Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

给定一个数组，第i个元素表示一个给定股票的第i天的价格。
设计一个算法，找到最大的利润。可以完成最多k个交易。
备注：
在再次买股票之前必须将股票卖出去。

Example 1:
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""


class Solution:
    def maxProfit(self, k: int, prices: list) -> int:
        """
        动态规划。
        维护两个数组：
        global[i][j] 表示在前i天内，完成最多j个交易，能获得的最大利润。
        local[i][j] 表示在前i天内，完成最多j个交易（且最后一次交易一定是在第i天卖出的）能获得的最大利润。
        子任务为：
        global[i][j] = max(global[i-1][j], local[i][j]) 即可以分为最后一天不卖和最后一天卖两种情况
        local[i][j] = max(global[i-1][j-1], global[i-1][j-1] + diff, local[i-1][j] + diff)
        :param k:
        :param prices:
        :return:
        """
        n = len(prices)
        if n <= 1 or k == 0:
            return 0
        global_list = [[0] * (k + 1) for _ in range(n)]
        local_list = [[0] * (k + 1) for _ in range(n)]
        for i in range(1, n):
            diff = prices[i] - prices[i - 1]
            for j in range(1, k + 1):
                local_list[i][j] = max(global_list[i - 1][j - 1] + max(diff, 0), local_list[i - 1][j] + diff)
                global_list[i][j] = max(global_list[i - 1][j], local_list[i][j])
        return global_list[-1][-1]

    def maxProfit2(self, k: int, prices: list) -> int:
        """
        动态规划，原理与第一个方法完全一样，只不过将二维数组改为了一维数组，降低空间复杂度.
        :param k:
        :param prices:
        :return:
        """
        n = len(prices)
        if n <= 1 or k == 0:
            return 0
        global_list = [0] * (k + 1)
        local_list = [0] * (k + 1)
        for i in range(1, n):
            diff = prices[i] - prices[i - 1]
            for j in range(k, 0, -1):
                # 观察maxProfit中的二维数组迭代式，可以发现，local_list[i][j]的表达式，两个二维数组都取的i-1，
                # global_list[i][j]的表达式，global_list取的i-1，local_list取的i
                # 因此，可以省去i这个维度，每次更新j这个维度，取i-1相当于就是取上一次循环的值，取i相当于取这一次循环之后的值
                # 对j的循环，必须是倒序，因为取上一次循环的值的时候，会取到j-1，如果是正序的话，j-1就只能取到最新值，因为已经覆盖了
                local_list[j] = max(global_list[j - 1] + max(diff, 0), local_list[j] + diff)
                global_list[j] = max(global_list[j], local_list[j])
        return global_list[-1]

    def maxProfit3(self, k: int, prices: list) -> int:
        """
        动态规划
        dp[i][j][0]：表示第i天交易了j次时卖出后的累计最大利润
        dp[i][j][1]：表示第i天交易了j次时买入后的累计最大利润
        迭代公式：
        dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1]+price[i])
        dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0]-price[i])
        """
        dp = [[[0, 0] for _ in range(k+1)] for __ in range(len(prices))]

        # 第一天，初始化：手里有股票则为 -price，手里没股票则收益为 0
        for j in range(k+1):
            dp[0][j][1] = - prices[0]

        # 第二天及以后，迭代
        for i in range(1, len(prices)):
            price = prices[i]
            for j in range(0, k+1):
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] - price)
                print('第{}天，交易{}次，持有股票，收益为{}'.format(i + 1, j, dp[i][j][1]))
                if j > 0:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + price)
                print('第{}天，交易{}次，清空股票，收益为{}'.format(i + 1, j, dp[i][j][0]))
        return dp[-1][-1][0]


    def maxProfit4(self, k: int, prices: list) -> int:
        """
        动态规划，与上面相同。
        由于等式左边都是i，等式右边都是i-1，所以可以将三维数组简化为二维，迭代公式为：
        dp[j][1] = max(dp[j][1], dp[j][0]-price)
        dp[j][0] = max(dp[j][0], dp[j-1][1]+price)
        但是j的遍历需要倒叙，因为第二个公式取 dp[j-1][1] 的时候，如果是正序，那么上一次循环刚刚计算了第 i 天的 dp[j-1][1]，
        但我们想要的是第 i-1 天的 dp[j-1][1]，所以倒叙遍历可以避免 j-1 被覆盖。
        （假如迭代公式中是 j+1， 而不是 j-1，那么则必须用正序。）
        """
        if k == 0 or len(prices) <= 1:
            return 0
        if k > len(prices) / 2:  # 最大交易数超过天数的一半，则等价于无限交易数，问题等价于第 122 题。
            result = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    result += prices[i] - prices[i-1]
            return result

        dp = [[0, 0] for _ in range(k+1)]

        # 第一天，初始化：手里有股票则为 -price，手里没股票则收益为 0
        for j in range(k+1):
            dp[j][1] = - prices[0]

        # 第二天及以后，迭代
        for price in prices[1:]:
            for j in range(k, -1, -1):
                dp[j][1] = max(dp[j][1], dp[j][0] - price)
                if j > 0:
                    dp[j][0] = max(dp[j][0], dp[j-1][1] + price)
        return dp[-1][0]


if '__main__' == __name__:
    k, prices = 2,  [3,3,5,0,0,3,1,4]
    print(Solution().maxProfit3(k, prices))

# -*- coding: utf-8 -*-

"""
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

有 N 个孩子站在一条线上。每个孩子有一个评价值。
你需要按照以下要求给这些孩子分发糖果：
1、每个孩子至少有一个糖果。
2、评价值更高的孩子会比他们的邻居得到更多的糖果。
你需要分发的最少糖果数是多少？

Example 1:
Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
"""

def candy(ratings: list) -> int:
    """
    从头开始遍历，如果当前比左边的大，那么当前值为左边加一，否则当前值为1，并且当前值左边的递减子序列每一个元素值都+1。
    """
    if not ratings:
        return 0
    
    cur_list = [1] * len(ratings) # 每个小孩已分发的糖果数
    cur_value = 1 # 当前小孩的糖果数
    top_idx = -1 # 递减子序列的前一个索引（或者说是上一个递增子序列的最后一个索引）
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]: # 递增
            cur_value += 1
            top_idx = i
        else: # 非递增
            cur_value = 1
            if ratings[i] < ratings[i - 1]: # 严格递减
                for j in range(top_idx + 1, i): # 从 top_idx+1 到 i 的每个元素都需要+1，因为 top_idx+1 到 i 是一个递减序列
                    cur_list[j] += 1
                if ratings[top_idx] > ratings[top_idx + 1]:
                    cur_list[top_idx] = max(cur_list[top_idx], cur_list[top_idx + 1] + 1) # 保证top_idx比右邻大
            else:
                top_idx = i - 1 # 左邻与当前值相等，那么当前值的大小不会受到左邻值的限制，所以要进行切割
        cur_list[i] = cur_value
    return sum(cur_list)

def candy2(ratings: list) -> int:
    """
    上一个方法的改进版。
    免去了for j in range(top_idx + 1, i)这一个循环，额外增加了对所有糖果的计数。
    """
    if not ratings:
        return 0
    total = 1
    cur_list = [1] * len(ratings) # 每个小孩已分发的糖果数
    cur_value = 1 # 当前小孩的糖果数
    top_idx = -1 # 递减子序列的前一个索引（或者说是上一个递增子序列的最后一个索引）
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]: # 递增
            cur_value += 1
            top_idx = i
        else: # 非递增
            cur_value = 1
            if ratings[i] < ratings[i - 1]: # 严格递减
                total += i - top_idx - 1 # 从 top_idx+1 到 i 的每个元素都需要+1，因为 top_idx+1 到 i 是一个递减序列
                if i - top_idx - 1 > 0:
                    cur_list[top_idx + 1] += 1 # 本来是应该top_idx+1 到 i 的每个元素都+1的，但是现在只给最左边的+1，因为中间的元素值大小没有作用
                if top_idx > -1 and ratings[top_idx] > ratings[top_idx + 1] and cur_list[top_idx] <= cur_list[top_idx + 1]: # 保证top_idx比右邻大
                    total += cur_list[top_idx + 1] - cur_list[top_idx] + 1
                    cur_list[top_idx] = cur_list[top_idx + 1] + 1
            else:
                top_idx = i - 1 # 左邻与当前值相等，那么当前值的大小不会受到左邻值的限制，所以要进行切割
        cur_list[i] = cur_value
        total += cur_value
    return total

if '__main__' == __name__:
    ratings = [1,3,2,2,1]
    print(candy2(ratings))
# -*- coding: utf-8 -*-

"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:
If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.

在一个环形道路上有 N 个加油站，加油站 i 的容量为 gas[i]。
你有一辆车，可以加无限量的油，从加油站 i 到下一个加油站 i+1 需要消耗油量 cost[i]。
你从其中一个加油站开始旅程，车的油箱为空。
返回可以按照顺时针完成一次环形旅行的起始加油站序号，否则返回 -1。

备注：
如果存在解，则此解是唯一解。
两个输入数组都是非空的，且长度相同。
输入数组的每个元素都是一个非负整数。

Example 1:
Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: 
gas  = [2,3,4]
cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""

def canCompleteCircuit(gas: list, cost: list) -> int:
    """
    暴力破解，依次试验每个起始站点。
    时间复杂度为O(n^2)
    """
    n = len(gas)
    for i in range(n): # 依次试验每个起始站点
        tank = 0 # 车箱容量
        j = i
        for _ in range(n): # 环行一周需要走n次
            tank += gas[j] - cost[j] # 先加油，再开往下个站点
            if tank < 0: # 油量不够开往下个站点
                break
            j += 1 # 到达下个站点
            if j >= n:
                j = 0
        else: # 没有break过，说明成功环行一周
            return i
    return -1

def canCompleteCircuit2(gas: list, cost: list) -> int:
    """
    两次遍历。
    第一次遍历，寻找可能的起始站点begin。假设起始站点为0，汽车开始跑，每当遇到油量为负，则更新起始站点为i+1，因为前面的任何一个当做起始站点都会成为负的。
    第二次遍历，检验begin是否真的满足需求。因为begin赋值是因为前面的站点不符合要求，但begin本身是否符合要求就不一定了。但如果begin都不符合要求，那么没有其他站点能够符合要求。
    """
    # 一次遍历，寻找可能的起始站点begin
    n = len(gas)
    tank = 0
    begin = 0
    for i in range(n):
        tank += gas[i] - cost[i]
        if tank < 0: # 每当遇到油量为负，则更新起始站点为i+1
            tank = 0
            begin = i + 1  if i + 1 < n else 0
    # 第二次遍历，检验起始站点begin是否满足需求
    tank = 0
    i = begin
    for _ in range(n):
        tank += gas[i] - cost[i]
        if tank < 0:
            return -1
        i = i + 1  if i + 1 < n else 0
    return begin

def canCompleteCircuit3(gas: list, cost: list) -> int:
    """
    两次遍历的改良版，变为一次遍历。
    第一次遍历时，额外统计total油箱剩余油量。
    第二次遍历可以省去，因为：如果gas之和大于等于cost之和，则必定至少有一个解。
    因此第一次遍历之后，只需要看total的正负即可。
    """
    n = len(gas)
    tank = 0
    begin = 0
    total = 0
    for i in range(n):
        tank += gas[i] - cost[i]
        total += gas[i] - cost[i]
        if tank < 0: # 每当遇到油量为负，则更新起始站点为i+1
            tank = 0
            begin = i + 1  if i + 1 < n else 0
    return begin if total >= 0 else -1

if '__main__' == __name__:
    gas  = [3,3,4]
    cost = [3,4,4]
    print(canCompleteCircuit3(gas, cost))
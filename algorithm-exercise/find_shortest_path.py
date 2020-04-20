# -*- coding: utf-8 -*-

"""
给定一个图，有向或无向，有环或无环。每个边有一个权重值，表示从一个点到另一个点的路径长度。
给定两个点 s 和 t，求从 s 到 t 的最短路径，每个节点最多经过一次。

权重用二维矩阵 W 描述，节点的名称为 0,1,2,...,len(W)-1。
W[i][j] 表示节点i到节点j的长度，如果为MAX则表示不通。
默认 s 为第一个节点。

实现了4种算法：
1、深度或广度搜索（可以解决一切问题，包括权重为负值的情况、有负权重回路的情况）
2、Dijkstra算法（只能解决权重为正数的情况）
3、Floyd算法（可以解决权重为负值的情况，不能解决有负权重回路的情况）
4、Bellman-Ford算法（可以解决权重为负值的情况，不能解决有负权重回路的情况）
"""
MAX = float('inf')

def dfs(W, t):
    """
    深度优先遍历。
    因为是全部遍历，且每个节点强制只遍历一次，所以可以解决一切问题，包括权重为负值的情况、有负权重回路的情况。
    """
    def fun(cur_list, cur_sum, result):
        """
        递归。
        cur_list：当前已走过的路径
        cur_sum：已走过路径的长度
        result：[path_list, sum]，存放最短路径和最短路径长度
        """
        # 递归结束条件
        if cur_list[-1] == t: # 寻找到终点
            if cur_sum < result[1]:
                result[0] = cur_list
                result[1] = cur_sum
            return
        # 在尚未遍历过的节点中寻找可以与cur_node直接相连的节点，继续迭代
        cur_node = cur_list[-1]
        for node in range(len(W)):
            if node not in cur_list and W[cur_node][node] < MAX: # 继续向前走一个节点
                fun(cur_list + [node], cur_sum + W[cur_node][node], result)
    result = [[], MAX]
    fun([0], 0, result)
    return result

def bfs(W, t):
    """
    广度优先遍历。
    因为是全部遍历，且每个节点强制只遍历一次，所以可以解决一切问题，包括权重为负值的情况、有负权重回路的情况。
    """
    result = [[], MAX]
    stack = [([0], 0)] # 先进先出队列，元素为 (已走路径，已走路径长度)
    while(stack):
        # 取出队列第一个元素
        cur_list, cur_sum = stack.pop(0)
        # 判断是否到了终点
        if cur_list[-1] == t:
            if cur_sum < result[1]:
                result[0] = cur_list
                result[1] = cur_sum
            continue
        # 向前走一步，然后把所有可能的结果都追加到队列末尾
        for i in range(len(W)):
            cur_node = cur_list[-1] # 路径的最后一个节点
            if i not in cur_list and W[cur_node][i] < MAX:
                stack.append((cur_list + [i], cur_sum + W[cur_node][i]))
    return result    

def dijkstra(W, t):
    """
    Dijkstra算法
    时间复杂度为 O(n^2)，空间复杂度为 O(n),空间复杂度不考虑存储path。
    """
    dist = [MAX] * len(W) # 存放最小距离
    dist[0] = 0
    path_list = [[0] for _ in W] # 存放最短路径，起点均为0
    T = {0} # 存放已计算出最小距离的节点
    min_idx = 0 # T 中最小距离节点
    while(t not in T):
        # 遍历不在T中的、且与 min_idx 直接相连的节点，计算当前距离（不一定是最小距离）
        for i, w in enumerate(W[min_idx]):
            if i not in T and W[min_idx][i] < MAX:
                new_idst = dist[min_idx] + W[min_idx][i] # 经过 min_idx 再到 i
                if new_idst < dist[i]: # 比历史到i的距离小
                    dist[i] = new_idst # 更新最小距离
                    path_list[i] = path_list[min_idx] + [i] # 更新最短路径
        # 遍历不在T中的节点，将距离最小的节点加入到T中，此时这个节点的当前距离便是最终的最小距离
        min_dist = MAX
        for i, d in enumerate(dist):
            if i not in T and d < min_dist:
                min_idx = i
                min_dist = d
        T.add(min_idx)
    return [path_list[t], dist[t]]

import copy
def floyd(W, t):
    """
    Floyd算法。
    第一次循环，任意两点之间只允许经过第1个节点进行中转，计算出任意两点之间的最小距离；
    第二次循环，任意两点之间只允许经过前两个节点进行中转，在上一次循环的基础上，计算出任意两点之间的最小距离；
    ...
    循环len(W)次，则任意两点自荐允许经过所有节点进行中转，同时得到了任意两点之间的最小距离。
    
    本方法能且只能同时解决任意两点之间的距离。
    时间复杂度为 O(n^3)，空间复杂度为 O(n^2).空间复杂度不考虑存储path。
    可以解决权重为负值的情况，前提是不存在负权重回路。
    """
    # 二维矩阵，定义任意两点之间的距离
    dist = copy.deepcopy(W)
    # 二维矩阵，定义任意两点之间的最短路径
    path = [[''] * len(W) for _ in W]
    for i in range(len(W)):
        for j in range(len(W)):
            if W[i][j] < MAX: # i和j直接相连
                path[i][j] = [i] if i == j else [i, j]
    # 开始迭代
    for k in range(len(W)):
        for i in range(len(W)):
            for j in range(len(W)):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[i][k] + path[k][j][1:]
    return path[0][t], dist[0][t]

def Bellman_Ford(W, t):
    """
    Bellman_Ford算法。
    第一次循环，计算任意一点到s点之间的距离，只允许经过1条边。
    第一次循环，计算任意一点到s点之间的距离，只允许经过2条边...
    循环n-1次，则得到了任意一点到s点之间的距离，允许经过n-1条边。
    连接两个点所需要最多的边数为n-1条边，因此只需要循环n-1次。
    时间复杂度为 O(nm)，空间复杂度为 O(n+m)。空间复杂度不考虑存储path。
    n为节点数，m为边数。
    可以解决权重为负值的情况，前提是不存在负权重回路。
    """
    # 根据权重矩阵，提取出所有边
    edge_list = [] # [(起点, 终点, 权重)]
    for i in range(len(W)):
        for j in range(len(W)):
            if i != j and W[i][j] < MAX:
                edge_list.append((i, j, W[i][j]))
    # 开始循环
    dist = [MAX] * len(W) # s点到任一点的距离
    dist[0] = 0
    path_list = [[0] for _ in W] # 存放最短路径，起点均为0
    for _ in range(len(W)-1):
        for edge in edge_list:
            if dist[edge[0]] + edge[2] < dist[edge[1]]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                path_list[edge[1]] = path_list[edge[0]] + [edge[1]]
    return path_list[t], dist[t]

if '__main__' == __name__:
    # 权重均为正
    W = [[0,9,4,MAX],
         [9,0,3,1],
         [4,3,0,1],
         [MAX,1,1,0]]
    # 有向无环负权重
    W = [[0,9,4,MAX],
         [9,0,MAX,-8],
         [4,3,MAX,1],
         [MAX,MAX,MAX,MAX]]
    t = 3
    print(dfs(W, t))
    print(bfs(W, t))
    print(dijkstra(W, t)) # 不支持负权重
    print(floyd(W, t))
    print(Bellman_Ford(W, t))
            

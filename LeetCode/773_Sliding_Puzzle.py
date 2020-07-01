# -*- coding: utf-8 -*-
"""
在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。

输入：board = [[4,1,2],[5,0,3]]
输出：5
解释：
最少完成谜板的最少移动次数是 5 ，
一种移动路径:
尚未移动: [[4,1,2],[5,0,3]]
移动 1 次: [[4,1,2],[0,5,3]]
移动 2 次: [[0,1,2],[4,5,3]]
移动 3 次: [[1,0,2],[4,5,3]]
移动 4 次: [[1,2,0],[4,5,3]]
移动 5 次: [[1,2,3],[4,5,0]]
"""

class Solution:
    def slidingPuzzle(self, board) -> int:
        '''
        宽度优先遍历
        :param board:
        :return:
        '''
        def swap(s, i, j):
            l = list(s)
            l[i], l[j] = l[j], l[i]
            return ''.join(l)

        neighbors = ((1, 3), (0, 4, 2), (1, 5), (0, 4), (3, 1, 5), (4, 2))
        visited_set = set()
        queue = []

        # 初始化
        start = ''.join([''.join([str(t) for t in x]) for x in board])
        target = '123450'
        queue.append(start)
        visited_set.add(start)
        step = 0

        # 宽度优先遍历
        while queue:
            n = len(queue)
            for i in range(n): # 遍历query所有情况
                cur = queue[i]
                if cur == target:
                    return step
                zero_idx = cur.find('0')
                for nei in neighbors[zero_idx]:
                    new_board = swap(cur, nei, zero_idx)
                    if new_board not in visited_set:
                        visited_set.add(new_board)
                        queue.append(new_board)
            queue = queue[n:]
            step += 1
        return -1

if '__main__' == __name__:
    board = [[4, 1, 2], [5, 0, 3]]
    print(Solution().slidingPuzzle(board))

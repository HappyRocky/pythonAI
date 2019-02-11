# -*- coding: utf-8 -*-

'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

给定一系列不重复的区间，要求将一个新的区间插入到这些集合中（如果有必要，则合并）。
可以假设这些区间已经根据起始位置排好序了。

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

def insert(intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    result = []
    # 查询新的区间应该插入的地方
    i = 0
    for i in range(len(intervals)):
        if intervals[i][0] >= newInterval[0]:
            break
        result.append(intervals[i])
    
    # 处理剩下的区间
    for cur_inter in [newInterval] + intervals[i:]:
        if result and cur_inter[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], cur_inter[1])
        else:
            result.append(cur_inter)
    
    return result

if '__main__' == __name__:
    intervals = []
    newInterval = [4,8]
    print(insert(intervals, newInterval))
            
# -*- coding: utf-8 -*-

'''
Given a collection of intervals, merge all overlapping intervals.

给定一个区间的数组，将所有重叠的区间进行合并。

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    先按照每个区间的起点排序，然后从小到大扫描。
    每次扫描，查看与前一个是否有重叠，如果是则合并成1个。
    这种方法只需要查看与前一个是否重叠，不需要查看更往前的，因为之前的都处理完毕。
    """
    intervals_sorted = sorted(intervals, key=lambda x : x[0])
    result = []
    for interval in intervals_sorted:
        # result中最后一个区间的右值>=新区间的左值，说明两个区间有重叠
        if result and result[-1][1] >= interval[0]:
            # 将result中最后一个区间更新为合并之后的新区间
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result

if '__main__' == __name__:
    intervals = [[1,4],[4,5]]
    print(merge(intervals))
        
    
    
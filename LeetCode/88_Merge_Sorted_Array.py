# -*- coding: utf-8 -*-
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，变成一个有序数组。
备注：
两个数组包含的初始元素个数分别为 m 和 n，可以认为， nums1 有足够的空间（大于等于 m+n）来容纳额外的来自 nums2 的元素。

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
def merge(nums1: list, m: int, nums2: list, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    归并排序，但是需要在nums1上直接操作。
    可以先将nums1的前m个元素右移n位，然后从第0位开始存放归并排序的结果，就不会发生冲突了。
    """
    if n == 0:
        return
    if m == 0:
        nums1[:n] = nums2[:n]
        return
    # nums1 右移n位
    nums1[n:n+m] = nums1[0:m]
    nums1[0:n] = [0] * n
    # 归并排序
    p1 = n # nums1的指针
    p2 = 0 # nums2的指针
    p = 0 # 合并结果的指针
    while(True):
        # 取较小值
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums1[p1]
            p1 += 1
        else:
            nums1[p] = nums2[p2]
            p2 += 1
        p += 1
        # 是否有一个数组到结尾
        if p1 == m + n or p2 == n:
            break
    if p1 == m + n:
        nums1[p:m+n] = nums2[p2:n]

if '__main__' == __name__:
    nums1 = [1,2,3,4,0,0,0]
    m = 4
    nums2 = [2,5,6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)

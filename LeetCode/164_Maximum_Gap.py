# -*- coding: utf-8 -*-

"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
Return 0 if the array contains less than 2 elements.
Note:
You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.

给定一个未排序的数组，返回其排序后的数组中相邻元素之差最大的值。
如果数组元素个数小于2，则返回0。
备注：
可以假设所有的元素都是非负整数。
时间和空间复杂度都要是线性的。

Example 1:
Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
             
Example 2:
Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.


"""

def maximumGap(nums: list) -> int:
    """
    桶排序是线性排序，非负整数正好用桶排序。
    """
    if not nums or len(nums) < 2:
        return 0
    # 求出最大值和最小值
    up = nums[0]
    down = nums[0]
    for num in nums:
        up = max(up, num)
        down = min(down, num)
    # 求出桶容量
    size = (up - down + 1) // len(nums) + 1
    # 放入桶中
    bucket_list = [[up + 1, -1]] * len(nums) # 每个桶存放最大值和最小值，[min, max]
    for num in nums:
        idx = (num - down) // size # 落在了哪个桶
        bucket_list[idx] = [min(bucket_list[idx][0], num), max(bucket_list[idx][1], num)]
    # 相邻桶的最大值和最小值的差距
    max_diff = 0
    pre = -1
    for bucket in bucket_list:
        if bucket[1] != -1: # 这个桶中有元素
            if pre != -1:
                max_diff = max(max_diff, bucket[0] - pre)
            pre = bucket[1]
    return max_diff

if '__main__' == __name__:
    nums = [3,6,9,1]
    print(maximumGap(nums))
    
    
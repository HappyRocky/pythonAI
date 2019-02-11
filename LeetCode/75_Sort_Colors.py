# -*- coding: utf-8 -*-

'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.

给定一个序列，包含 n 个颜色为红，白或蓝的物体。将他们进行排序，希望相同颜色的物体是相邻的，并且颜色顺序为红，白，蓝。
我们使用 0，1，2 分别代表颜色 红，白，蓝。
备注：不能使用系统自带的排序函数。

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

'''
def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    计数法。
    先扫描一遍，统计0，1，2每个数字的个数。
    然后再扫描一遍，按照顺序将三个数字铺上去。
    """
    if not nums:
        return
    # 统计三个数字的个数
    count_list = [0,0,0] # 三个数字的计数
    for num in nums:
        count_list[num] += 1
    # 按顺序修改list
    begin = 0
    for i in range(len(count_list)):
        nums[begin:begin+count_list[i]] = [i] * count_list[i]
        begin += count_list[i]
        
def sortColors2(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    双指针法。
    维持首尾两个指针p1和p2，渐渐向中间移动，保证p1之前全为0，p2之后全为2。
    再维护一个指针p，从左向右扫描一遍，遇到0则和p1交换，遇到2则和p2进行交换，同时p1/p2向中间移动一格。
    当p与p2相遇时，说明扫描结束。
    这种方法只适用于3种颜色，如果是4种或更多，则不再适用。
    """
    if not nums:
        return
    p1 = 0
    p2 = len(nums) - 1
    for i in range(len(nums)):
        if i > p2:
            break
        while((nums[i] == 0 and i > p1) or (nums[i] == 2 and i < p2)):
            if nums[i] == 0:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            if nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1

if '__main__' == __name__:
    nums = [2,0,1]
    sortColors2(nums)
    print(nums)
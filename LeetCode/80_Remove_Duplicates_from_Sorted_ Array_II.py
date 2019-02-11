# -*- coding: utf-8 -*-

'''
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

给定一个有序数组，删除重复的数字，使得重复数字最多出现两次，返回新数组的长度。
不要开辟新的数组，只能在原数组中进行操作，空间复杂度为O(1)。

Example 1:
Given nums = [1,1,1,2,2,3],
Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It doesn't matter what you leave beyond the returned length.
Example 2:
Given nums = [0,0,1,1,1,1,2,3,3],
Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
It doesn't matter what values are set beyond the returned length.
'''
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    维护一个字典，存放每个字符出现的次数。
    维护一个索引p，保证索引左边所有字符个数都不超过2个。
    从左到右扫描，根据字典的字符次数，将尚未出现2次的字符放到索引p的位置，然后p向右移动一格。
    扫描一遍之后，从0到p的子数组，即为删除掉重复数字之后的数组。
    """
    count_dict = dict()
    p = 0
    for i in range(len(nums)):
        num = nums[i]
        count_dict[num] = count_dict.get(num, 0) + 1
        if count_dict[num] <= 2:
            nums[p] = nums[i]
            p += 1
    return p

if '__main__' == __name__:
    nums = [1,1,1,2,2,3]
    print(removeDuplicates(nums))
    
# -*- coding: utf-8 -*-

'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

给定一个数组和一个常量 val，删除数组中所有等于 val 的元素，返回新数组的长度。
不要为另外的数组去开辟新的空间，只能修改原数组，空间复杂度为O(1)。
元素的顺序可以改变。新数组之后的元素无关紧要。

Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
Note that the order of those five elements can be arbitrary.
It doesn't matter what values are set beyond the returned length.
'''

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    从左到右扫描，维护一个索引，这个索引始终保持为新数组的最后一位。
    如果扫描到了一个元素不等于val，则将索引+1，且索引对应的值修改为当前元素值。
    此方法不会改变数组的长度。
    """
    if not nums:
        return 0
    
    idx = 0
    for num in nums:
        if num != val:
            nums[idx] = num
            idx += 1
    return idx

if '__main__' == __name__:
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(removeElement(nums, val))


    
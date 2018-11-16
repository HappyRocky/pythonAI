# -*- coding: utf-8 -*-

'''

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

给定一个非负整数的数组，你一开始站在第一个索引的位置。
每一个元素表示从当前位置开始一次跳跃的最大长度。
判断你是否可以跳跃到最后一个索引位置。

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

'''

def canJump2(nums):
    """
    :type nums: List[int]
    :rtype: bool
    递归法。
    如果从倒数第二位置可以跳到倒数第一位置，那么，可以跳跃到倒数第一位置 <=> 可以跳跃到倒数第二位置。
    因此，使用递归寻找是否可以跳跃到倒数第二位置即可。
    如果从倒数第二位置跳不到倒数第一位置，则继续向前寻找倒数第三位置是否可以一步跳到倒数第一位置。
    依次向前查询，如果前面的元素全部都不能一步跳到倒数第一位置，则说明应该返回False。
    """
    
    def can_reach(j):
        '''
        判断是否可以到达索引j
        '''
        # 递归结束条件
        if j == 0:
            return True
        # 从后向前开始扫描，只要有其中一个位置可以从它开始跳到j，就可以继续递归
        for i in range(j-1, -1, -1):
            if nums[i] >= j - i:
                return can_reach(i)
        return False
    
    return can_reach(len(nums)-1)

if '__main__' == __name__:
    nums = [3,2,1,0,4]
    print(canJump2(nums))
        
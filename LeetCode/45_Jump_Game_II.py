# -*- coding: utf-8 -*-

'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
Note:
You can assume that you can always reach the last index.

给定一个非负整数的数组，你一开始站在第一个索引的位置。
每一个元素表示从当前位置开始一次跳跃的最大长度。
你的目标是用最少的跳跃次数到达最后一个索引位置。
输出跳跃次数。
备注：
假设肯定可以跳到最后一个位置。

Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

'''

def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    
    从后往前遍历一遍，找到可以跳到倒数第一位置的最左边的索引，步数+1.
    然后将这个索引当做跳跃的目标地点，记为end，从end开始向前遍历一遍，找到可以跳到end的最左边的索引，步数+1.
    重复这个过程，直至end==0为止，整个过程相当于从最后一位跳跃到了第一位。
    时间复杂度为O(n^2)
    
    """
    # 初始化end
    end = len(nums)-1
    step = 0
    
    # 开始从后向前跳跃
    while(end > 0):
        left = end
        for i in range(end - 1, -1, -1):
            if nums[i] >= end - i:
                left = min(left, i)
        end = left
        step += 1
    return step

def jump2(nums):
    """
    :type nums: List[int]
    :rtype: int
    
    改良版。
    上述方法每次更新end，都要重新遍历一遍end之前的所有元素，越靠前的元素，越容易被多次遍历，浪费时间。
    可以提前构造一个数组，里面存放着可以跳跃到当前位置的最左边的元素索引。
    这样，再按照上述方法的思想，从后向前寻找，每次寻找可以跳到end的最左边索引时，直接从数组中取即可。
    而构造这样一个数组，只需要遍历一遍即可。
    因此时间复杂度降为O(n)
    """
    
    # 构造数组
    l = len(nums)
    left_list = [-1] * l
    for i in range(l-2, -1, -1):
        # 从当前位置向后长度为nums[i]之中的每个位置，都可以由当前位置直接跳跃到
        # 由于是从后向前遍历，因此left_list上的同一索引的数只有可能被更小的数替代
        left_list[i+1:i+1+nums[i]] = [i] * nums[i]
    
    # 初始化end
    end = len(nums)-1
    step = 0
    
    # 开始从后向前跳跃
    while(end > 0):
        end = left_list[end]
        step += 1
    return step

def jump3(nums):
    """
    :type nums: List[int]
    :rtype: int
    从前向后跳跃。
    只需要一次扫描即可，从左向右扫描。
    维持三个变量：
    i：从左向右依次扫描
    end：当前位置可以跳跃到的最远距离
    farthest:在end之前的所有位置出发，可以跳跃到的最远距离
    
    从首位置开始，比如nums[0] = 5，那么第一步可以调到 1~5 的任一位置。
    记 end = 5。
    那么跳到哪个位置最好呢？
    如果 1-5 的某个位置可以保证从这个位置出发再跳跃一次可以达到最远，则这个位置是最好的。
    因此扫描1-5这5个位置，每扫描到一个，就记录下这个位置可以到达的最远距离，选择最大值，记为 farthest，可以跳跃到 farthest 的位置记为 j。
    然后当 i 扫描到 end 时，step+1，同时 end=farthest，表示刚才的一步已经从0跳跃到了 j，但是不用记录j的值，只需要步数正确即可。
    接下来继续扫描，从当前位置到end之间，不断更新 farthest。
    循环这个过程，直到 farthest 超过了倒数第一的位置，算法结束。
    
    算法复杂度为O(n)。
    """
        
    l = len(nums)
    if l <= 1:
        return 0
    end = 0
    farthest = 0
    step = 0
    for i in range(l):
        farthest = max(farthest, i + nums[i])
        if i == end:
            step += 1
            end = farthest
            if end >= l-1:
                break
    return step
    

if '__main__' == __name__:
    nums = [3,2,3,2,1,2,1]
    print(jump3(nums))
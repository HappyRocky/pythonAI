# -*- coding: utf-8 -*-

'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

给定一个序列，按照字典序，输出下一个序列，使得到的新数组的字典序恰好大于原数组。
如果不存在这样的排列，就将原数组从小到大排序。
替换必须就地进行，不要分配额外的内存。

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

'''

def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    
    首先从右向左遍历数组，找到第一个相邻的左<右的数对，记右下标为x，则左下标为x - 1
    若x > 0，则再次从右向左遍历数组，直到找到第一个大于nums[x - 1]的数字为止，记其下标为y，交换nums[x - 1], nums[y]
    最后将nums[x]及其右边的元素就地逆置
    
    """
    l = len(nums)
    
    # 从右向左查询第一个小于右邻的元素
    for i in range(l-2, -1, -1):
        if nums[i+1] > nums[i]:
            break
    else: # 没有找到，说明为降序排列
        nums[:] = nums[::-1]
        return
    
    # 从右向左查询第一个大于nums[i]的元素
    for j in range(l-1, -1, -1):
        if nums[j] > nums[i]:
            break
    
    # 交换i和j
    nums[i], nums[j] = nums[j], nums[i]            
    
    # i后面的序列进行反转
    nums[i+1:l] = nums[-1:i:-1]
    
if '__main__' == __name__:
    nums = [3,2,1]
    nextPermutation(nums)
    print(nums)
        
    
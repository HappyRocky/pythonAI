# -*- coding: utf-8 -*-

"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

给定一个大小为n的数组，找到主要元素。主要元素指的是出现次数超过了⌊ n/2 ⌋ 。
可以假设数组是非空的，并且主要元素一定存在。

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums) -> int:
        """
        利用字典进行计数
        :param nums:
        :return:
        """
        half = len(nums) // 2
        count_dict = dict()
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
            if count_dict[num] > half:
                return num
        return None


if '__main__' == __name__:
    solution = Solution()
    nums = [1]
    print(solution.majorityElement(nums))




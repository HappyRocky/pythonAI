# -*- coding: utf-8 -*-

'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

给定一个无重复元素的数组 candidates 和一个目标数 target，找到 candidates 中所有可以使数字之和等于 target 的组合。
数组中的每个元素只可以使用一次。
备注：
数组的元素和目标值都是正数。
答案中不能有重复组合。

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''

def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    回溯法。
    从列表中选择一个元素a，放入到结果池中。
    这样，剩下的任务就是从数组中挑选组合使得求和等于 target-a。
    因此，可以用递归方法继续执行子任务。
    如果任务最后完不成，则将元素a换成下一个元素b，继续执行新的子任务。
    """
    
    sorted_candidates = sorted(candidates)
    result_list = []
    def fun_rec(cur_result, start_idx, remain_value):
        '''
        找到可以满足相加等于remain的一个组合，
        与前缀cur_result连接，
        放入到result_list中
        '''
        if remain_value == 0: # 剩余恰好为0
            result_list.append(cur_result)
            return
        for i in range(start_idx, len(sorted_candidates)):
            value = sorted_candidates[i]
            if value > remain_value: # 之后的更大，更不会满足要求，不必继续循环
                break
            elif result_list and result_list[-1][0:len(cur_result)+1] == cur_result + [value]:
                # 避免结果重复
                start_idx = i + 1 # 避免一个元素多次使用
                continue
            else:
                fun_rec(cur_result + [value], i + 1, remain_value - value)
            
    fun_rec([], 0, target)
    return result_list

if '__main__' == __name__:
    candidates = [2,5,2,1,2]
    target = 5
    print(combinationSum2(candidates, target))
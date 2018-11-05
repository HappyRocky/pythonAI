# -*- coding: utf-8 -*-

'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

给定一个无重复元素的数组 candidates 和一个目标数 target，找到 candidates 中所有可以使数字之和等于 target 的组合。
candidates 中的数字可以无限制重复被选取。
备注：
数组的元素和目标值都是正数。
答案中不能有重复组合。

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

def combinationSum(candidates, target):
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
    def fun_rec(cur_result, remain):
        '''
        找到可以满足相加等于remain的一个组合，
        与前缀cur_result连接，
        放入到result_list中
        '''
        if remain == 0: # 剩余恰好为0
            result_list.append(cur_result)
            return
        for i in sorted_candidates:
            if i > remain: # 之后的更大，更不会满足要求，不必继续循环
                break
            elif not cur_result or i >= cur_result[-1]: # 避免重复
                fun_rec(cur_result + [i], remain - i)
            
    fun_rec([], target)
    return result_list

if '__main__' == __name__:
    candidates = [2,3,5]
    target = 8
    print(combinationSum(candidates, target))
                
 
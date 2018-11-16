# -*- coding: utf-8 -*-

'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

给定一系列数字，可能会包含重复数字，返回所有可能的唯一的排列。

Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''
    
def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    深度优先搜索。
    按照全排列的定义，每次分别从剩余的集合中取出一个，直至取完。
    注意，如果当前取出的一个，在之前已经取出过同样的元素值，则跳过，防止重复。
    """
    def get_rest(result_list, pre_list, rest_list):
        '''
        递归，对rest_list进行全排列，并分别与pre_list拼接，最终加入到result_list中
        '''
        if not rest_list:
            result_list.extend(pre_list)
        for i in range(len(rest_list)):
            if i > 0 and rest_list[i] == rest_list[i-1]: # 防止重复
                continue
            new_list = rest_list[:i] + rest_list[i+1:] # 去掉第i个元素
            get_rest(result_list, [x+[rest_list[i]] for x in pre_list], new_list)
         
    nums_sort = sorted(nums) # 排序，便于判断是否重复
    result_list = []
    get_rest(result_list, [[]], nums_sort)
    return result_list

def permuteUnique2(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    广度优先搜索。
    维护一个状态列表，里面的元素是所有状态词典，词典中有两个key，记录已经搜索到的和尚未搜索到的。
    每次循环，对于所有状态词典，对每个尚未搜索到的数字，都拼接到已经搜索到的数组的末尾，然后形成一个新的状态列表。
    这样，每次循环，所有状态词典中的已搜索到的序列长度+1，尚未搜索到的集合长度-1。
    因此，只需要循环 len(nums) 次，所有状态都表示搜索完毕了。
    """
    nums_sort = sorted(nums)
    state_list = [{'pre':[],'rest':nums_sort}]
    for _ in range(len(nums)): # 循环len(nums)次
        new_state_list = []
        for dic in state_list:
            rest_list = dic['rest']
            for i in range(len(rest_list)):
                if i > 0 and rest_list[i] == rest_list[i-1]: # 防止重复
                    continue
                new_list = rest_list[:i] + rest_list[i+1:] # 去掉第i个元素
                new_state_list.append({'pre':dic['pre']+[rest_list[i]],'rest':new_list})
        state_list = new_state_list
    return [x['pre'] for x in state_list]

def permuteUnique3(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    分治法。
    设nums的长度为n，则前n项的全排列 = 第n个数字依次插入到前n-1项的全排列的两两之间的缝隙中（包括首尾两端）。
    因此可以使用递归。
    """
    def get_permutes(n):
        '''
        得到nums前n项的全排列。
        '''
        # 递归结束条件
        if n == 1:
            return [[nums[0]]]
        
        # 得到前n-1项的全排列
        pre_list = get_permutes(n-1)
        # 将第 n 个元素，依次插入到 pre_list 中的元素缝隙中
        result_list = []
        for permute in pre_list:
            for i in range(len(permute)+1):
                if i > 0 and nums[n-1] == permute[i-1]: # 防止重复
                    # 不能是continue。一旦碰到相同数字，则后面所有空隙的插入都略过。
                    break
                result_list.append(permute[:i] + [nums[n-1]] + permute[i:])
        return result_list
    nums.sort()
    return get_permutes(len(nums))

if '__main__' == __name__:
    nums = [1,1,2,2]
    print(permuteUnique3(nums))
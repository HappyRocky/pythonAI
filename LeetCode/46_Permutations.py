# -*- coding: utf-8 -*-

'''
Given a collection of distinct integers, return all possible permutations.

给定一个无重复整数数组，返回所有可能的排列。

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
import copy
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    字典序法。
    不断寻找当前排序的下一个排序，直至寻找到了第一次的排序。
    """
    def nextPermutation(nums):
        """
        :type nums: List[int]
        
        首先从右向左遍历数组，找到第一个相邻的左<右的数对，记右下标为x，则左下标为x - 1
        若x > 0，则再次从右向左遍历数组，直到找到第一个大于nums[x - 1]的数字为止，记其下标为y，交换nums[x - 1], nums[y]
        最后将nums[x]及其右边的元素就地逆置
        
        """
        l = len(nums)
        result = copy.deepcopy(nums)
        # 从右向左查询第一个小于右邻的元素
        for i in range(l-2, -1, -1):
            if result[i+1] > result[i]:
                break
        else: # 没有找到，说明为降序排列
            result[:] = result[::-1]
            return result
        # 从右向左查询第一个大于nums[i]的元素
        for j in range(l-1, -1, -1):
            if result[j] > result[i]:
                break
        # 交换i和j
        result[i], result[j] = result[j], result[i]            
        # i后面的序列进行反转
        result[i+1:l] = result[-1:i:-1]
        return result
    
    if not nums:
        return []
    result = [nums]
    cur = nums
    while(True):
        cur = nextPermutation(cur)
        if cur == nums: # 回到了第一个
            break
        result.append(cur)
    return result

def permute2(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    深度优先搜索。
    按照全排列的定义，每次分别从剩余的集合中取出一个，直至取完。
    """
    def get_rest(result_list, pre_list, rest_set):
        '''
        递归，对rest_set进行全排列，并分别与pre_list拼接，最终加入到result_list中
        '''
        if not rest_set:
            result_list.extend(pre_list)
        for i in rest_set:
            get_rest(result_list, [x+[i] for x in pre_list], rest_set-{i})
            
    result_list = []
    get_rest(result_list, [[]], set(nums))
    return result_list

def permute3(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    广度优先搜索。
    维护一个状态列表，里面的元素是所有状态词典，词典中有两个key，记录已经搜索到的和尚未搜索到的。
    每次循环，对于所有状态词典，对每个尚未搜索到的数字，都拼接到已经搜索到的数组的末尾，然后形成一个新的状态列表。
    这样，每次循环，所有状态词典中的已搜索到的序列长度+1，尚未搜索到的集合长度-1。
    因此，只需要循环 len(nums) 次，所有状态都表示搜索完毕了。
    """
    state_list = [{'pre':[],'rest':set(nums)}]
    for _ in range(len(nums)): # 循环len(nums)次
        new_state_list = []
        for dic in state_list:
            for num in dic['rest']:
                new_state_list.append({'pre':dic['pre']+[num],'rest':dic['rest']-{num}})
        state_list = new_state_list
    return [x['pre'] for x in state_list]

def permute4(nums):
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
                result_list.append(permute[:i] + [nums[n-1]] + permute[i:])
        return result_list
    return get_permutes(len(nums))

if '__main__' == __name__:
    nums = [1,2,3]
    print(permute4(nums))
        
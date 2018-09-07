# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 09:21:35 2018

@author: gongyanshang1

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

给定一个字符串，包含了2~9的整数，要求返回所有可能的数字对应的字母组合。
每一个数字都对应一些字母，和电话拨号器相对应，如下：

1      2abc   3def
4ghi   5jkl   6mno
7pqrs  8tuv   9wxyz
*+     0      #

示例：
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

下面提出了3种算法，其中后两种算法效率最高，第一种最慢。

"""

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    如果digits的长度是固定的，比如3，那么我们可以写3个for循环，每个循环取某一位的所有可能字符，进行枚举。
    但问题是长度不固定，不知道要写几个for循环。
    可以重新考虑一种遍历方法，类似于数学上的手算加法，每次在个位+1，如果溢出则需要进位。
    比如：digits='27'，分别含有3个和4个字母。
    则定义一个两位数，个位满4进1，十位满3进1。
    从00开始遍历，每次+1，直至最高位溢出为止。
    等价地，为了便于编码，可以从最高位开始+1，直至最低位溢出为止。
    """
    
    if not digits:
        return []
    
    # 获取每一位的所有可能子母
    letters = []
    nums = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    for i in digits:
        letters.append(nums[int(i)])
    indexs = [0] * len(digits) # 初始化索引集合
    result = []
    while(True):
        # 将当前索引对应的字母加入到结果中
        tmp = ''
        for i,j in enumerate(indexs):
            tmp += letters[i][j]
        result.append(tmp)
        # 索引+1
        overflow = 0
        for i in range(len(indexs)):
            if i == 0: # 最高位+1
                indexs[0] += 1
            else: # 其他位加上进位1
                indexs[i] += overflow
            if indexs[i] >= len(letters[i]): # 溢出，下一位进1
                indexs[i] -= len(letters[i])
                overflow = 1
            else:
                overflow = 0
        if overflow == 1: # 说明最后一位也溢出了，则遍历结束
            break
    return result

def letterCombinations2(digits):
    """
    :type digits: str
    :rtype: List[str]
    分治法，递归。
    将字符串分为两部分，两部分的所有情况进行笛卡尔积，就是所求结果。
    """
    nums = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    if not digits:
        return []
    
    def fun_rec(l, u):
        '''
        寻找digits[l~u]之间的所有可能性
        '''
        # 递归结束条件
        if l > u:
            return []
        if l == u:
            return list(nums[int(digits[l])])
        
        # 分为两部分，分别得到遍历结果，然后整合
        mid = int((l + u) / 2)
        result1 = fun_rec(l, mid)
        result2 = fun_rec(mid+1, u)
        result = []
        for str1 in result1:
            for str2 in result2:
                result.append(str1 + str2)
        return result
    return fun_rec(0, len(digits)-1)

def letterCombinations3(digits):
    """
    :type digits: str
    :rtype: List[str]
    动态规划。
    不断使用笛卡尔积：
    前k位的遍历结果（长度为n），分别都加上第k+1位的所有情况（长度为m），就得到了前k+1位的遍历结果（长度为n*m）。
    """
    if not digits:
        return []
    nums = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    result = []
    for i in digits:
        if not result:
            result = list(nums[int(i)])
        else:
            tmp = []
            for p in nums[int(i)]: # 遍历当前位的所有字母
                for exist in result: # 遍历之前的结果
                    tmp.append(exist + p)
            result = tmp
    return result

if '__main__' == __name__:
    digits = '237'
    print(letterCombinations3(digits))
    
    
    
    
 
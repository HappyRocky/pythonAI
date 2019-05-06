# -*- coding: utf-8 -*-

"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

包含字母A-Z的字符串，可以使用以下映射编码为数字：
'A' -> 1
'B' -> 2
...
'Z' -> 26

给定一个非空字符串，只包含数字，判断所有可能的解码方法的个数。

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

def numDecodings(s: str) -> int:
    """
    广度优先遍历
    """
    result_list = [s] # [remain_str]
    count = 0
    # 将remain_str进行切分
    while result_list:
        for i in range(len(result_list) - 1, -1, -1): # 倒序遍历，方便在末尾进行增删
            remain_str = result_list[i]
            del result_list[i]
            if not remain_str: # 没有剩余元素，切分完毕
                count += 1
            elif remain_str[0] == '0': # 第一个元素为0，无法切分
                continue
            elif len(remain_str) == 1: # 只剩一个元素了，切分完毕，增加了一种切分方法
                count += 1
            elif remain_str[1] == '0': # 只能将前两个元素一起切分出去，不能分开
                if remain_str[0] >= '3':
                    continue
                result_list.append(remain_str[2:])
            else:
                result_list.append(remain_str[1:])
                if int(remain_str[:2]) <= 26:
                    result_list.append(remain_str[2:])
    return count

def numDecodings2(s: str) -> int:
    """
    深度优先遍历，回溯法
    """
    def fun(cur_list, remain_str, result_list):
        """
        将remain_str进行切分，切分的所有结果都分别附在cur_str之后
        result_list存放所有切分完毕的成果
        """
        if not remain_str:
            result_list.append(cur_list)
        elif remain_str[0] != '0': # 第一个元素为0，无法切分
            fun(cur_list + [remain_str[0]], remain_str[1:], result_list) # 切分第一个元素
            if len(remain_str) > 1 and int(remain_str[:2]) <= 26: # 切分前两个元素
                fun(cur_list + [remain_str[:2]], remain_str[2:], result_list)
    result_list = []
    fun([], s, result_list)
    print(result_list)
    return len(result_list)

def numDecodings3(s: str) -> int:
    """
    分治法
    """
    if not s:
        return 1
    if s[0] == '0':
        return 0
    if len(s) == 1:
        return 1
    # 分为两部分，各自计算次数： 0 1 2 ... mid-1 | mid mid+1 ... len(s)-1
    mid = int(len(s) / 2)
    result = 0 if s[mid] == '0' else numDecodings3(s[:mid]) * numDecodings3(s[mid:])
    # 考虑两部分的分界线的左右两个字符被分到一组中的情况
    if mid > 0 and s[mid-1] != '0' and (mid == len(s)-1 or s[mid+1] != '0') and int(s[mid-1:mid+1]) <= 26:
        result += numDecodings3(s[:mid-1]) * numDecodings3(s[mid+1:])
    return result

def numDecodings4(s: str) -> int:
    """
    一次扫描。
    每扫描到一个新元素，就判断：1、本身是否可以单独划分出来 2、和前面一个字符结合，是否可以划分出来
    """
    v, w, p = 0, int(s>''), '' # w是方法个数，v是上一个循环的方法个数，d是当前字符，p是前一个字符
    for d in s:
        v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
    return w

from functools import reduce 
def numDecodings5(s):
    """
    将上述方法用一行实现
    """
    return reduce(lambda t,d : (t[1], (d>'0')*t[1]+(9<int(t[2]+d)<27)*t[0], d), s, (0, s>'',''))[1]*1

if '__main__' == __name__:
    s = '43214213416346576476711101186432413414'
    print(numDecodings5(s))
        
                
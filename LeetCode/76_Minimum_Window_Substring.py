# -*- coding: utf-8 -*-

'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

给定一个字符串 S 和 字符串 T，找到 S 中的最短子串，这个子串包含 T 中所有的字符。时间复杂度为 O(n)。

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

备注：
如果 S 中没有这种子串，则返回空字符串。
如果有这种子串，则可以假设在 S 中只有唯一的最小子串。
'''
import copy
def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    递归法。
    记 s(i) 为 s 的长度为 i 的前缀子串。
    记 d(i) 为 s(i) 的包含 t 所有字符的最小子串。
    则 d(i) 可以通过 d(i-1) 递推出来。
    假设 s(i) 的包含 t 所有字符的最小后缀为 h(i)，则 d(i) 等于 d(i-1) 和 s(i) 中较短的那个。
    """
    def find_min_suffix(ss, char_set):
        '''
        寻找 ss 的包含char_set所有字符的最短后缀
        '''
        if len(ss) < len(char_set):
            return ''
        for i in range(len(ss)-1,-1,-1):
            if ss[i] in char_set:
                char_set.remove(ss[i])
            if not char_set:
                break
        else: # 没有break过
            return ''
        return ss[i:]
    
    # 获取t中的字符
    char_set = set(list(t))
    
    # 寻找包含t所有字符的最短前缀
    prefix = find_min_suffix(s[::-1], copy.copy(char_set))[::-1]
    
    # 寻找 prefix 中包含t所有字符的最短后缀
    suffix = find_min_suffix(prefix, copy.copy(char_set))
    
    # 开始遍历
    min_sub = suffix
    for i in range(len(prefix), len(s)):
        cur_suffix = find_min_suffix(s[:i+1], copy.copy(char_set))
        if len(cur_suffix) < len(min_sub):
            min_sub = cur_suffix
    return min_sub

def minWindow2(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    动态规划法。
    记 s(i) 为 s 的长度为 i 的前缀子串。
    记 d(i) 为 s(i) 的包含 t 所有字符的最小子串。
    则 d(i) 可以通过 d(i-1) 递推出来。
    假设 s(i) 的包含 t 所有字符的最小后缀为 h(i)，则 d(i) 等于 d(i-1) 和 s(i) 中较短的那个。
    """
    if len(s) < len(t):
        return ''
    # 统计t中的字符个数
    char_dict = dict()
    for char in t:
        char_dict[char] = char_dict.get(char, 0) + 1
    
    # 开始遍历
    store_dict = dict() # 统计扫描过的t中的字符个数
    full_count = 0 # 统计扫描过的t中已够数的字符类型数
    cur_start = 0 # 当前子串的起始位置
    min_start = 0 # 最短子串的起始位置
    min_length = len(s)+1 # 最短子串的长度
    for i in range(len(s)):
        char = s[i]
        if char not in char_dict: #不属于t，继续遍历
            continue
        store_dict[char] = store_dict.get(char, 0) + 1 # 计数
        if store_dict[char] != char_dict[char]: # 可能不够，也可能超过
            continue
        full_count += 1 # 加1之后刚好等于，说明增加了一个已够数的字符类型
        while(full_count == len(char_dict)): # 从子串的最左边开始逐个去除，直至子串不再满足包含t的所有字符
            if i - cur_start + 1 < min_length: # 当前子串是满足要求的，因此需要和历史最短子串比较并更新
                min_start = cur_start
                min_length = i - cur_start + 1
            start_char = s[cur_start]
            cur_start += 1 # 去掉子串的第一个字符
            if start_char not in char_dict:
                continue
            store_dict[start_char] -= 1 # 去掉第一个字符的影响
            if store_dict[start_char] < char_dict[start_char]:
                full_count -= 1
    if min_length > len(s):
        return ''
    return s[min_start:min_start+min_length]

if '__main__' == __name__:
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow2(s, t))
    
# -*- coding: utf-8 -*-

'''
Given an array of strings, group anagrams together.
Note:
All inputs will be in lowercase.
The order of your output does not matter.

给定一个字符串数组，将所有字符串分组，每一组的字符串包含的字符相同但是顺序不同。

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

'''

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    排序法。
    对每个字符串，先排序，然后作为key，将原字符串加入到key对应的value中。
    排序的算法复杂度为 O(nlogn)，因此整体算法复杂度为 O(mnlogn)。
    m为字符串个数，n为每个字符串的平均长度。
    """
    dic = dict()
    for s in strs:
        key = str(sorted(s))
        dic[key] = dic.get(key, []) + [s]
    return list(dic.values())

def groupAnagrams2(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    计数法。
    对每个字符串，对包含的字符的种类和个数进行统计，然后将同样记录结果的字符串聚集在一起。
    相当于也是用了排序法，只不过是桶排序，算法复杂度为O(n)，因此整体算法复杂度为O(mn)。
    """
    dic = dict()
    for s in strs:
        l = [0] * 26 # 26个字母的计数
        for char in s:
            l[ord(char) - ord('a')] += 1
        key = str(l)
        dic[key] = dic.get(key, []) + [s]
    return list(dic.values())

from functools import reduce 
def groupAnagrams3(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    累乘法。
    找到同一组内的所有字符串的共同点作为key：每个字符对应素数的累乘。
    使用了定理：如果一个数的一种因数分解的结果全部是素数，那么这种因数分解是唯一的分解方法。
    缺点：乘积结果与字符串长度成指数增长，容易数据溢出。
    整体算法复杂度为O(mn)。
    """
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    dic = dict()
    for s in strs:
        if s:
            char_to_primes = [prime_list[ord(char) - ord('a')] for char in s]
            key = reduce(lambda x,y : x*y, char_to_primes)
        else:
            key = 0
        dic[key] = dic.get(key, []) + [s]
    return list(dic.values())

if '__main__' == __name__:
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams3(strs))
    
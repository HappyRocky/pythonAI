# -*- coding: utf-8 -*-

'''
You are given a string, s, and a list of words, words, that are all of the same length. 
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

给定一个字符串s、一个数组words，里面元素都是一个词，所有词的长度相等。
在s中寻找所有子串的索引，子串需要是words中每个词首尾拼接而成，词之间没有其他字符插入，词的拼接顺序没有要求。

Example 1:
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []

思路：
1、暴力法
由于每个词长度相等，因此每次取出子串的长度是固定的，而且很容易计算出所有词语拼接起来的长度。
假设所有词拼接起来的长度为 len。
定义一个指针，从左往右遍历s，每次遍历都判断当前指针开始往后的长度为 len 的子串是否符合要求：
1、对子串按照词语长度进行切分，分成候选词语，候选词语的个数为数组 words 的词语个数。
2、对于每一个候选词语，都与数组 words 中的词语进行匹配，如果正好可以一一匹配上，则说明符合要求。
小技巧：
可以将words中的每个词的个数提前统计出来，每次匹配上一个，个数-1，直至所有的词的个数都变为0，则说明匹配成功。

2、改进版
当某个分词匹配不上words时，所有包含这个分词的子串肯定都是不符合要求的，可以迅速忽略掉。
比如一个子串 'aaabbbccc'，被切分成了3个候选词语 'aaa','bbb','ccc'，
然后依次与words中的词语进行匹配，结果发现words中并没有 'ccc' 这个词语，于是这个子串匹配失败。
但是我们还可以获得一个信息，就是当指针继续向右移动3次，需要判断 'bbbcccddd' 这个子串是否符合要求时，
我们可以迅速知道肯定是不符合要求的，因为这个子串也会切分出 'ccc' 这个词语。
关键点在于，是指针向右移动 3 次之后的子串可以迅速判断不符合要求，这个 3 便是每个词语的长度。
因此，从当前指针开始，到匹配不上的候选词语的起始位置结束，这之间的子串，按照词语长度进行切割，得到每个词语的起始位置，以这些位置开头的子串都不符合条件，可以迅速略过。

'''

import copy
import re

def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    暴力法。
    从左往右遍历s，每次遍历都判断当前指针往后的子串是否符合要求。
    有几个技巧：
    1、由于每个词长度相等，因此每次取出子串的长度是固定的，而且可以将子串提前进行切分。
    2、可以将words中的每个词的个数提前统计出来，然后每次遍历时将子串切分的结果挨个进行匹配，直到每个词都匹配了应该有的个数。
    """
    if not s or not words:
        return []
    
    l_word = len(words[0]) # 每个词的长度
    l_total = l_word * len(words) # 所有词拼接起来的长度
    
    if len(s) < l_total: # s长度小于所有词拼接起来的长度
        return []
    
    # 统计words中的词频
    word_count_dict = dict()
    for word in words:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    
    # 遍历s
    result = []
    for i in range(0, len(s) - l_total + 1):
        cur_dict = copy.copy(word_count_dict)
        split_list = re.findall(f'.{{{l_word}}}', s[i:i+l_total]) # 按词长度切割子串
        for split_word in split_list:
            if split_word in cur_dict: # 可以匹配上words中的某个词
                if cur_dict[split_word] > 1: # 次数-1
                    cur_dict[split_word] -= 1
                else:
                    cur_dict.pop(split_word)
                # 如果词典为空，则说明全部匹配了一遍
                if not cur_dict:
                    result.append(i)
            else: # 匹配不上，说明当前子串不合格
                break
    return result

def findSubstring2(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    改进版。
    当某个分词匹配不上words时，所有包含这个分词的子串肯定都是不符合要求的，可以迅速忽略掉。
    """
    if not s or not words:
        return []
    
    l_word = len(words[0]) # 每个词的长度
    l_total = l_word * len(words) # 所有词拼接起来的长度
    
    if len(s) < l_total: # s长度小于所有词拼接起来的长度
        return []
    
    # 统计words中的词频
    word_count_dict = dict()
    for word in words:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    
    # 遍历s
    result = []
    ignore_idx_set = set() # 肯定不符合要求的索引
    for i in range(0, len(s) - l_total + 1):
        if i in ignore_idx_set:
            continue
        cur_dict = copy.copy(word_count_dict)
        for j in range(0, len(words)): # 每次遍历子串的一个分词
            split_word_start = i + j*l_word # 分词的起始索引
            split_word = s[split_word_start : split_word_start + l_word] # 子串的第j个分词
            if split_word in cur_dict: # 可以匹配上words中的某个词
                if cur_dict[split_word] == 0: # 次数已经用尽，说明此词是多余的，子串不符合要求
                    break
                cur_dict[split_word] -= 1
                if j == len(words) - 1: # 已经遍历完最后一个分词，说明子串符合要求
                    result.append(i)
            else: # 分词不存在于words中，则所有包含这个分词的子串都肯定不符合要求
                k = i + l_word # 包含这个分词的子串的起始位置
                while(k <= split_word_start):
                    ignore_idx_set.add(k)
                    k += l_word
                break
    return result

if '__main__' == __name__:
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    print(findSubstring2(s, words))
    
    
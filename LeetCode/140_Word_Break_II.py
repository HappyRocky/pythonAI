# -*- coding: utf-8 -*-

"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
add spaces in s to construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences.
Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

给定一个非空字符串 s 和一个非空单词数组 wordDict。
在 s 中添加空格，来构造一句话，每个单词都是一个有效的数组中的单词。
返回所有可能的句子。
备注：
字典中同一个单词可能会使用多次。
可以假设字典中不包含重复单词。

Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

def wordBreak(s: str, wordDict:list) -> list:
    """
    深度优先遍历
    """
    def fun(s, wordDict, cur_list, result_list):
        """
        递归，深度优先遍历。
        将 s 进行一次拆分，如果成功，则加入到 cur_list 中，剩下的部分递归。
        如果恰好拆分结束，加入到 result_list 中。
        """
        # 递归结束条件
        if not s:
            result_list.append(' '.join(cur_list))
            return
        # 尝试拆分
        for w in wordDict:
            if w == s[:len(w)]:
                fun(s[len(w):], wordDict, cur_list + [w], result_list)
    result_list = []
    fun(s, wordDict, [], result_list)
    return result_list

def wordBreak2(s: str, wordDict:list) -> list:
    """
    深度优先遍历，改进之处在于存储每个子字符串的划分结果。
    """
    def fun(s, i, memo):
        """
        计算子字符串 s[i:] 的划分结果
        memo 存放每个 i 的划分结果
        """
        if i not in memo:
            memo[i] = [s[i:j] + (' ' + rest if rest else '')
                        for j in range(i+1, len(s)+1)
                        if s[i:j] in wordDict
                        for rest in fun(s, j, memo)]
        return memo[i]
    return fun(s, 0, {len(s):['']})

if '__main__' == __name__:
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(wordBreak2(s, wordDict))
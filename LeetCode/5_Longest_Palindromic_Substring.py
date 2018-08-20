# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 09:36:15 2018

@author: gongyanshang1

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

给定一个字符串s，找到s中最长的回文字字符串。假设s的最大长度为1000.

示例：
Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"

"""

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    
    暴力求解。扫描所有子字符串，分别判断是否为回文字符串，返回最长的回文字符串。
    时间复杂度为O(n^3)
    """
    
    def is_palindromic(a):
        '''
        a是否为回文字符串
        '''
        b = a[::-1]
        if a == b:
            return True
        return False
    
    max_substr = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j+1]
            if is_palindromic(substr) and len(substr) > len(max_substr):
                max_substr = substr
    return max_substr

def longestPalindrome2(s):
    """
    :type s: str
    :rtype: str
    
    暴力求解的优化：每次判断一个字符串是否是回文字符串时，p(s[i:j]) = p(s[i+1:j-1]) && s[i] == s[j]。
    将每次的判断结果存存起来，之后再用就不用重新计算了。
    但需要从后向前遍历，这样才会用得到提前存储的结果。
    时间复杂度为O(n^2)。
    """
    
    if len(s) <= 1:
        return s
    
    def is_palindromic(a, dic):
        '''
        a是否为回文字符串
        '''
        result = False
        if len(a) == 1:
            result = True
        elif len(a) == 2:
            result = a[0] == a[1]
        else:
            b = a[1:-1]
            if b in dic:
                result = dic[b] and a[0] == a[-1]
            else:
                b = a[::-1]
                if a == b:
                    result = True
        dic[a] = result
        return result
    
    max_substr = ''
    dic = dict()
    for i in range(len(s)-1, -1, -1):
        for j in range(i, len(s)):
            substr = s[i:j+1]
            if is_palindromic(substr, dic) and len(substr) > len(max_substr):
                max_substr = substr
    return max_substr


if '__main__' == __name__:
    s_list = ["cyyoacmjwjubfkzrrbvquqkwhsxvmytmjvbborrtoiyotobzjmohpadfrvmxuagbdczsjuekjrmcwyaovpiogspbslcppxojgbfxhtsxmecgqjfuvahzpgprscjwwutwoiksegfreortttdotgxbfkisyakejihfjnrdngkwjxeituomuhmeiesctywhryqtjimwjadhhymydlsmcpycfdzrjhstxddvoqprrjufvihjcsoseltpyuaywgiocfodtylluuikkqkbrdxgjhrqiselmwnpdzdmpsvbfimnoulayqgdiavdgeiilayrafxlgxxtoqskmtixhbyjikfmsmxwribfzeffccczwdwukubopsoxliagenzwkbiveiajfirzvngverrbcwqmryvckvhpiioccmaqoxgmbwenyeyhzhliusupmrgmrcvwmdnniipvztmtklihobbekkgeopgwipihadswbqhzyxqsdgekazdtnamwzbitwfwezhhqznipalmomanbyezapgpxtjhudlcsfqondoiojkqadacnhcgwkhaxmttfebqelkjfigglxjfqegxpcawhpihrxydprdgavxjygfhgpcylpvsfcizkfbqzdnmxdgsjcekvrhesykldgptbeasktkasyuevtxrcrxmiylrlclocldmiwhuizhuaiophykxskufgjbmcmzpogpmyerzovzhqusxzrjcwgsdpcienkizutedcwrmowwolekockvyukyvmeidhjvbkoortjbemevrsquwnjoaikhbkycvvcscyamffbjyvkqkyeavtlkxyrrnsmqohyyqxzgtjdavgwpsgpjhqzttukynonbnnkuqfxgaatpilrrxhcqhfyyextrvqzktcrtrsbimuokxqtsbfkrgoiznhiysfhzspkpvrhtewthpbafmzgchqpgfsuiddjkhnwchpleibavgmuivfiorpteflholmnxdwewj"]
    for s in s_list:
        result = longestPalindrome2(s)
        print(f'{s}\t{result}')
                
    
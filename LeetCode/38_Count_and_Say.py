# -*- coding: utf-8 -*-

'''
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.

数数并说序列是一个整数序列，第二项起每一项的值为对前一项的记数，其前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 读作 “1个1”，即 11
11 读作 “两个1”，即 21
21 读作 “一个2，一个1”，即 1211

给定一个整数n，1 ≤ n ≤ 30，生成数数并说序列的第 n 项。
备注：该整数序列的每一项都输出为字符串。

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
'''

def countAndSay(n):
    """
    :type n: int
    :rtype: str
    递归法。
    """
    
    # 递归结束条件
    if n == 1:
        return "1"
    
    # 递归获得前一项
    # 末尾加上哨兵值，保证输出所有记数
    pre = countAndSay(n-1) + '.'
    
    # 开始遍历
    tmp = pre[0]
    count = 1
    result = ''
    for i in range(1, len(pre)):
        if pre[i] == tmp: # 与前一项相同
            count += 1
        else: # 与前一项不同，则输出
            result += str(count) + tmp
            tmp = pre[i]
            count = 1
    
    return result

if '__main__' == __name__:
    n = 5
    print(countAndSay(n))
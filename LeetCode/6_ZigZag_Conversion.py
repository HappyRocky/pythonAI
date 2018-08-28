# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 09:15:23 2018

@author: gongyanshang1

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

给定行数，字符串"PAYPALISHIRING"可以写成之字形：
P   A   H   N
A P L S I I G
Y   I   R
然后，一行一行地读："PAHNAPLSIIGYIR"
要求编写一个函数，输入一个字符串和行数，改写为之字形后，输出按行读的结果。

示例：
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I


"""

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    
    模拟法。
    先初始化一个二维数组，当做一个平面，然后按照之字形规则依次摆放每个元素，最后按行读取。
    为了方便，我们将之字形由竖版改为横版：
    PAYP
      A
     L
    ISHI
      R
     I
    NG
    
    """
    
    if len(s) <= numRows or numRows == 1:
        return s
    
    # 画出之字形
    plot = []
    direction = 1 # 画笔方向，1为右，0为左0
    plot.append(['']*numRows) # 初始化第一行
    i = 0
    j = -1
    for idx in range(len(s)):
        if direction == 1: # 向右，则行不变，列+1
            j += 1
            plot[i][j] = s[idx]
            if j == numRows - 1: # 到头了，则往回走
                direction = 0
        else: # 向左，则行+1，列-1
            plot.append(['']*numRows) # 新添加一行
            i += 1
            j -= 1
            plot[i][j] = s[idx]
            if j == 0:
                direction = 1
    # 按列输出
    output = ''
    for j in range(numRows):
        for i in range(len(plot)):
            output += plot[i][j]
    return output

def convert2(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    
    直接输出法。
    可以找到规律，每 2*numRows-2 一个周期。
    
    0     6      12 
    1   5 7   11 13
    2 4   8 10
    3     9
    
    """
    
    if len(s) <= numRows or numRows == 1:
        return s
    
    period = 2*numRows-2
    output = s[0]
    i = 0
    count = 1
    while(count < len(s)):
        # 寻找下一个
        rest = i % period
        if rest == 0 or rest == numRows - 1: # 位于第一行或最后一行
            i += period    
        elif rest <  numRows - 1: # 位于竖行
            i += (numRows - rest - 1) * 2
        else: # 位于斜行
            i += (period - rest) * 2
        # 如果溢出则换行
        if i >= len(s):
            if rest <= numRows - 1:
                i = rest + 1
            else:
                i = period - rest + 1
                
        # 赋值
        output += s[i]
        count += 1
    
    return output
                
if '__main__' == __name__:
    s = 'ABCD'
    n = 3
    print(convert(s, n))
    print(convert2(s, n))
        
    
    
    


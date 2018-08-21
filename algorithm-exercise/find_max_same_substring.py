# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:44:42 2018

@author: gongyanshang1

寻找两个字符串的最长公共子串的长度
"""

def find_max_same_substr(s1, s2):
    '''
    动态规划。
    定义一个矩阵，比较矩阵中每个点对应的行列字符是否相等，相等的话置为左上邻+1，不相等置为0
    矩阵正最大的数即为所求长度。
    示例：
    s1 = 'abcd'
    s2 = 'bca'
    矩阵为：
      a b c d
    b 0 1 0 0
    c 0 0 2 0
    a 1 0 0 0 
    因此最长公共子串的长度为2。
    '''
    if len(s1) == 0 or len(s2) == 0:
        return 0
    
    # 矩阵，高为s1长度，宽为s2长度
    flag_matrix = []
    max_len = 0
    for i in range(len(s1)):
        flag_matrix.append([])
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i > 0 and j > 0:
                    flag_matrix[i].append(flag_matrix[i-1][j-1] + 1)
                else:
                    flag_matrix[i].append(1)
            else:
                flag_matrix[i].append(0)
            max_len = max(max_len, flag_matrix[i][j])
    return max_len

if '__main__' == __name__:
    s1 = 'abcd'
    s2 = 'bca'
    print(find_max_same_substr(s1,s2))

# -*- coding: utf-8 -*-

"""
实现gray code（格雷编码）
"""

def get_gray_code_list(n:int) -> list:
    """
    给定格雷编码长度n（正整数），返回按顺序排列的格雷编码列表。
    递归实现，规则：
    n+1位格雷码的集合 = n位格雷码集合(顺序)加前缀0 + n位格雷码集合(逆序)加前缀1
    """
    # 递归结束条件
    if n == 1:
        return ['0', '1']
    # 开始递归
    l = get_gray_code_list(n-1)
    return ['0' + x for x in l] + ['1' + x for x in l[::-1]]

def get_next_gray_code(cur_code:str) -> str:
    """
    给定某一个格雷编码，返回下一个格雷编码.
    """
    return ''

def int_to_graycode(n:int) -> int:
    """
    十进制下，整数转格雷编码
    规则：
    1、n右移一位，高位补0，得到m
    2、n和m异或
    """
    return (n >> 1) ^ n

def binary_to_graycode(binary:str) -> str:
    """
    二进制数转格雷编码（编码）
    规则：
    记：
    自然二进制码为B(n-1)B(n-2)...B(2)B(1)B(0)
    二进制格雷码为G(n-1)G(n-2)...G(2)G(1)G(0)
    则：
    最高位保留  B(n-1)=(Gn-1)
    其他位 G(i) = B(i) xor B(i+1)
    """
    result = binary[0]
    for i in range(1, len(binary)):
        result += str(int(binary[i]) ^ int(binary[i-1]))
    return result

def graycode_to_binary(code:str) -> int:
    """
    格雷编码转二进制（解码）
    规则：
    记：二进制格雷码为G(n-1)G(n-2)...G(2)G(1)G(0)
    自然二进制码为B(n-1)B(n-2)...B(2)B(1)B(0)
    则：
    最高位保留  B(n-1)=(Gn-1)
    其他位 B(i) = G(i) xor B(i+1)
    """
    result = code[0]
    for i in range(1, len(code)):
        result += str(int(code[i]) ^ int(result[-1]))
    return result
    
if '__main__' == __name__:
    n = 5
    print(get_gray_code_list(n))
    print(int_to_graycode(n))
    print(binary_to_graycode('101'))
    print(graycode_to_binary('111'))
    
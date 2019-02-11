# -*- coding: utf-8 -*-

'''
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: 
It is intended for the problem statement to be ambiguous. 
You should gather all requirements up front before implementing one. 
However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

判断一个字符串是否可以被翻译为一个小数。
备注：
问题描述是模棱两可的。你需要收集所有的实现方式。
在一个有效的小数中，可能存在的字符有：
1、数字0-9
2、正负号 +/-
3、小数点 .
当然，这些符号的上下文也是很关键的。

'''
import re
def isNumber(s):
    """
    :type s: str
    :rtype: bool
    通过示例可以看出一些规则：
    1、首尾的多个空格可以忽略
    2、正负号不能相邻
    3、如果有出现了e，那么e前面可以是小数，e后面只能是整数（可以是负数）
    4、除了e，不能出现其他任何字母
    5、"1." 或者 ".1" 都认为是正确的小数
    """
    s = s.strip()
    p1 = r'([0-9]+)' # 整数
    p2 = r'(([0-9]+)?\.([0-9]+))' # 小数，.前面可以为空
    p3 = r'(([0-9]+)\.)' # 小数，.后面为空
    p4 = f'((\+|-)?({p1}|{p2}|{p3}))' # 小数或整数的正则表达式
    p5 = f'^({p4}|({p4}e(\+|-)?{p1}))$' # 只有小数，或者e前面为小数，e后面为整数
    if re.match(p5, s):
        return True
    else:
        return False
        
if '__main__' == __name__:
    s = ""
    print(isNumber(s))
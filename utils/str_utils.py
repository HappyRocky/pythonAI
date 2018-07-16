# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 10:17:19 2018

@author: gongyanshang1

字符串操作工具类
"""

import re

def is_int(string):
    '''
    判断一个字符串是否完全由数字组成
    '''
    return string.isdigit()

def is_number(string):
    '''
    判断一个字符串是否是一个数字（包括正负数、整数、小数、科学计数法）
    如：True：'1','0.1','+1','-1.2','1.234e-3'
    '''
    try:
        float(string)
    except:
        return False
    return True

def is_english(string):
    '''
    判断一个字符串是否完全由英文字母组成
    '''
    pattern=r'^[a-zA-Z]+$'
    return re.match(pattern, string) is not None

def is_english_number(string):
    '''
    判断一个字符串是否只包含数字或英文字母
    '''
    pattern=r'^[a-zA-Z0-9]+$'
    return re.match(pattern, string) is not None

if '__main__' == __name__:
    print(is_english_number('adsf32safd.4a'))



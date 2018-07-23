# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 15:15:35 2018

@author: gongyanshang1

测试装饰器
"""

# 不带参数的装饰器（被装饰函数有参数）
# =============================================================================
# def add_one(f):
#     def fun(*args):
#         a = args[0]
#         f(a + 1)
#     return fun
# 
# @add_one
# def print_self(a):
#     print("a =", a)
#    
# print_self(1)
# =============================================================================

# 不带参数的装饰器（被装饰函数无参数）
# =============================================================================
# def add_one(f):
#     print('excute add_one')
#     return f
# 
# @add_one
# def print_self():
#     print("excute print_self")
#    
# print_self()
# =============================================================================


# 带参数的装饰器（被装饰函数有参数）
# =============================================================================
# def add_number(num):
#     def fun(f):
#         def _fun(*args):
#             f(args[0] + num)
#         return _fun
#     return fun
# 
# @add_number(2)
# def print_b(b):
#     print('b =', b)
# 
# print_b(1)
# =============================================================================

# 带参数的装饰器（（被装饰函数无参数））
def add_number(num):
    def fun(f):
        print('num =', num)
        return f
    return fun

@add_number(2)
def print_hello():
    print('hello')

print_hello()



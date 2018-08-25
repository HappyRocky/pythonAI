# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 15:20:05 2018

@author: gongyanshang1

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

给定两个非空链表，表示两个非负整数。每个节点代表一位数字，且以倒序存放。
要求对两个数相加，并把结果也用链表展示出来。
假设两个整数不以0开头，除非整数本身就等于0。

示例：
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

class ListNode:
    def __init__(self, x):
        
        if isinstance(x, list):
            self.val = x[0]
            self.next = None
            head = self
            for i in range(1, len(x)):
                head.next = ListNode(x[i])
                head = head.next
        else:
            self.val = x
            self.next = None
        
    def output(self):
        '''
        输出链表
        '''
        result = str(self.val)
        head = self.next
        while(head is not None):
            result += f' -> {head.val}'
            head = head.next
        return '(' + result + ')'
        
def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    
    def fun_rec(ll1, ll2, overflow):
        '''
        递归函数，返回两个链表相加的结果
        '''
        # 递归结束
        if ll1 is None and ll2 is None:
            if overflow == 1:
                return ListNode(1)
            else:
                return None
        
        # 确定两个相加的值
        if ll1 is None:
            num1 = 0
            next_code1 = None
        else:
            num1 = ll1.val
            next_code1 = ll1.next
        if ll2 is None:
            num2 = 0
            next_code2 = None
        else:
            num2 = ll2.val
            next_code2 = ll2.next
        
        # 得到相加结果
        s = num1 + num2 + overflow
        if s > 9:
            s = s - 10
            overflow = 1
        else:
            overflow = 0
        
        # 返回
        new_node = ListNode(s)
        new_node.next = fun_rec(next_code1, next_code2, overflow)
        return new_node
    
    return fun_rec(l1, l2, 0)

def create_list(nums):
    '''
    将数组转为链表
    '''
    head = ListNode(nums[0])
    p = head
    for i in range(1, len(nums)):
        p.next = ListNode(nums[i])
        p = p.next
    return head

if '__main__'     == __name__:
    l1 = ListNode([2,4,3])
    l2 = ListNode([5,6,6,2,1])
    print(f'{l1.output()} + {l2.output()} = {addTwoNumbers(l1,l2).output()}')
        
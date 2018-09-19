# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:32:06 2018

@author: gongyanshang1

Given a linked list, swap every two adjacent nodes and return its head.
Note:
Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.

给定一个链表，将每两个相邻的节点交换位置，最后返回头结点。
备注：
算法只能使用常量的空间。
不可以修改节点的值，只能改变节点本身。

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.

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
    
def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    
    """
    head2 = ListNode(0)
    head2.next = head
    p = head2
    while(p and p.next and p.next.next):
        p2 = p.next
        p3 = p2.next
        p2.next = p3.next
        p.next = p3
        p3.next = p2
        p = p2
    return head2.next

if '__main__' == __name__:
    head = ListNode([1])
    print(swapPairs(head).output())
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 09:26:13 2018

@author: gongyanshang1

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.

给定一个链表，每k个节点一组进行组内反转，返回修改后的链表。
k是一个正数，且小于等于列表的长度。
如果节点数不是k的整数倍，则最后剩余的节点需要保持原样。
备注：
只能使用常量的内存。
不能改变节点的值，只能修改节点本身。

Example:
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

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

def reverseKGroup(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    递归，只要剩余链表长度大于等于k，则将前k个进行反转，然后继续处理剩下的链表。
    """
    def fun_rec(p):
        '''
        :type p: ListNode
        从链表p的下一位开始，每k个一组进行组内反转。
        '''
        # 链表长度是否大于等于k
        p0 = p
        c = 0
        while(c < k and p.next):
            p = p.next
            c += 1
        if c < k:
            return p
        pe = p # 将第k个保存起来
        pe2 = pe.next # 将第k+1个保存起来
        p1 = p0.next # 将第1个保存起来，作为下一次递归的参数
        p0.next = pe # 首指针指向第k个
        
        # 开始循环反转前k个链表
        c = 0
        p = p1
        next = pe2
        while(c < k):
            p_next = p.next
            p.next = next
            next = p
            p = p_next
            c += 1
        fun_rec(p1) # 继续处理剩下的链表
    if k == 1 or not head:
        return head
    head0 = ListNode(0)
    head0.next = head
    fun_rec(head0)
    return head0.next
    
if '__main__' == __name__:
    head = ListNode([1,2,3,4,5])
    k = 1
    print(reverseKGroup(head, k).output())
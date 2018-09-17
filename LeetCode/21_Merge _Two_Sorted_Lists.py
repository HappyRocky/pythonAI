# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 10:24:30 2018

@author: gongyanshang1

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

合并两个有序链表，返回一个新链表。即合并排序。

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
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

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    归并排序。
    定义两个指针，分别指向两个链表的head。
    然后依次取出指针值，比较大小，将较小值追加到新链表，同时将较小值所在链表的指针往后移动一位。
    如果其中一个指针到头了，那么将另一个指针剩下的链表直接追加到新链表即可。
    直至两个指针都指到了最后一位。
    """
    
    if not l1:
        return l2
    if not l2:
        return l1
    
    p1 = l1
    p2 = l2
    head = ListNode(0)
    p = head
    while(p1 and p2):
        if p1.val < p2.val:
            p.next = ListNode(p1.val)
            p1 = p1.next
        else:
            p.next = ListNode(p2.val)
            p2 = p2.next
        p = p.next
    if p1:
        p.next = p1
    elif p2:
        p.next = p2
    return head.next

if '__main__' == __name__:
    l1 = ListNode([1,2,3])
    l2 = ListNode([1,3,4])
    print(mergeTwoLists(l1,l2).output())
        
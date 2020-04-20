# -*- coding: utf-8 -*-

"""
Write a program to find the node at which the intersection of two singly linked lists begins.

找到两个单向链表的交叉部分的起始节点。

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
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
    
def getIntersectionNode(headA, headB):
    """
    :type headA, headB: ListNode
    :rtype: ListNode
    """
    if not headA or not headB:
        return None
    pa, pb = headA, headB
    while(pa != pb): # 每次两个指针都各自前进一步，但凡有一个到头了，就切换成另一个链表的头部，继续走。如果有一个切换过，那么过不了多久另一个肯定会切换。并且切换之后，肯定会正好在交叉点会合。
        pa = pa.next if pa else headB
        pb = pb.next if pb else headA
    return pa

    
    
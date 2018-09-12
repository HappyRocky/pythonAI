# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 09:28:48 2018

@author: gongyanshang1

Given a linked list, remove the n-th node from the end of list and return its head.

给定一个链表，删除倒数第n个节点，返回头部。
备注：
可以认为n总是有效的。

示例：
输入: 1->2->3->4->5, and n = 2.
输出：1->2->3->5.

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

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    从头部开始遍历所有节点，指针为p，同时维护第二个指针p2，使得p2总是落后p指针n个节点。
    这样，当p到达末尾时，p2恰好到达倒数第n个节点，可以直接删除。
    """
    if not head or n == 0:
        return head
    
    p = head
    p2 = None
    count = 0
    while(p.next):
        p = p.next
        if p2:
            p2 = p2.next
        else:
            count += 1
            if count == n:
                p2 = head
    
    # 此时，p指向最后一个节点，p2指向倒数第 n+1 个节点
    if p2: # p2被赋值
        p2.next = p2.next.next
    else: # p2为空，说明还没有给p2赋值，要删除的节点为head节点
        head = head.next
    return head

if '__main__' == __name__:
    l = ListNode([1,2,3,4,5])
    n = 4
    print(removeNthFromEnd(l, n).output())
            
    
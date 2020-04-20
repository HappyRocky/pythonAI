# -*- coding: utf-8 -*-

"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
Note: Do not modify the linked list.

给定一个链表，返回环路的起始节点。如果没有环路，则返回null。
为了表示这个环，我们使用一个整数 pos 来代表表尾连接的索引位置。
备注：不要修改这个环。
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
            
def detectCycle(head):
    """
    遍历一遍，直至出现了重复的节点，此节点即为环路的起始节点。
    """
    p = head
    node_set = set()
    while(p):
        if p in node_set:
            return p
        node_set.add(p)
        p = p.next
    return None
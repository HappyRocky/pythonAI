# -*- coding: utf-8 -*-

"""
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

给定一个链表，判断是否存在一个环。
为了表示这个环，我们使用一个整数 pos 来代表表尾连接的索引位置。
如果 pos = -1，说明没有环。

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
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
            
def hasCycle(head):
    """
    遍历一遍，直至遍历到重复节点
    """
    p = head
    node_set = set()
    while(p):
        if p in node_set:
            return True
        node_set.add(p)
        p = p.next
    return False



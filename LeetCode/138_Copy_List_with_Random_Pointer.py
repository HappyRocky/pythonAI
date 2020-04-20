# -*- coding: utf-8 -*-

"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.

给定一个链表，每个节点包含一个额外的随机指针，可能会指向链表中的任一节点或指向空。
返回这个链表的深3拷贝。

Example 1:
Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.

Note:
You must return the copy of the given head as a reference to the cloned list.
"""
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
        
def copyRandomList(head: Node) -> Node:
    """
    先将每个节点的深拷贝对象存储起来
    然后根据“拷贝的next=next的拷贝”对拷贝节点进行连接
    """
    d = dict()
    m = n = head
    while(m):
        d[m] = Node(m.val, None, None)
        m = m.next
    while(n):
        d[n].next = d.get(n.next)
        d[n].random = d.get(n.random)
        n = n.next
    return d.get(head)

import collections
def copyRandomList2(head: Node) -> Node:
    """
    只遍历一遍即可。
    遍历到每个节点时，将源节点的next和random的拷贝都赋给拷贝的next和random。
    如果还不存在拷贝，则新建一个，此时不知道值为多少，那么就val=0。反正早晚会遍历到这个节点，到时候给拷贝节点赋值也不迟。
    """
    d = collections.defaultdict(lambda : Node(0, None, None))
    d[None] = None
    n = head
    while(n):
        d[n].val = n.val
        d[n].next = d[n.next]
        d[n].random = d[n.random]
        n = n.next
    return d[head]
    

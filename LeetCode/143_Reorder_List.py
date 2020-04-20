# -*- coding: utf-8 -*-

"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.

给定一个链表 L: L0→L1→…→Ln-1→Ln
将其转化为：L0→Ln→L1→Ln-1→L2→Ln-2→…
不能修改节点的值，只能修改节点本身。

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
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
            
def reorderList(head: ListNode) -> None:
    """
    遍历一遍，将链表转为数组，然后进行转化
    """
    # 链表转为数组
    p = head
    node_list = []
    while(p):
        node_list.append(p)
        p = p.next
    # 递归转化
    def fun(i, j):
        """
        将 node_list 的第i个和第j个索引之间的数组转化为链表
        """
        # 迭代终止条件
        if i > j:
            return None
        if i == j:
            node_list[i].next = None
            return node_list[i]
        # 返回：i -> j -> 剩余的
        node_list[i].next = node_list[j]
        node_list[j].next = fun(i+1, j-1)
        return node_list[i]
    fun(0, len(node_list) - 1)

if '__main__' == __name__:
    head = ListNode([1,2,3,4])
    reorderList(head)
    print(head.output())
    
    
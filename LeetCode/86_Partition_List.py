# -*- coding: utf-8 -*-

'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

给定一个链表和一个值 x，将链表进行划分，使得所有小于 x 的节点在前，大于等于 x 的节点在后。
这两个部分内的节点顺序需要保持和之前的顺序一直。

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''
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
    
    
def partition(head: ListNode, x: int) -> ListNode:
    '''
    维护2个链表，分别按顺序存放小于x的节点和大于等于x的节点
    然后把这2个链表串起来。
    '''
    p1_head = ListNode(0) # 存放小于x的节点
    p2_head = ListNode(0) # 存放大于等于x的节点
    p1 = p1_head
    p2 = p2_head
    while(head):
        if head.val < x: # 小于x，追加到p1
            p1.next = head
            head = head.next
            p1 = p1.next
            p1.next = None
        else: # 否则，追加到p2
            p2.next = head
            head = head.next
            p2 = p2.next
            p2.next = None
    p1.next = p2_head.next # p1尾部连接p2头部
    return p1_head.next

if '__main__' == __name__:
    head = ListNode([1,4,3,2,5,2])
    x = 3
    print(partition(head, x).output())

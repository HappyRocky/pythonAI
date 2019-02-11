# -*- coding: utf-8 -*-

'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

给定一个有序链表，将所有重复节点删掉，保证每个元素只出现一次。

Example 1:
Input: 1->1->2
Output: 1->2
Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
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
    
def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    从头开始遍历，如果next的值等于当前值，则将next节点删除。
    """
    p = head
    while(p and p.next):
        if p.next.val == p.val:
            p.next = p.next.next
        else:
            p = p.next
    return head
        
if '__main__' == __name__:
    head = ListNode([1,1,2,3,3,3])
    head = deleteDuplicates(head)
    print(head.output())

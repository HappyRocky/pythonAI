# -*- coding: utf-8 -*-

'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

给定一个链表，将其向右旋转k次，k为非负值。

Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
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

def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    定义两个指针p1和p2，都从头开始遍历链表。
    p2始终落后p1 k 个位置。
    那么当p1走到末尾时，p2正好走到倒数第k个位置。
    将p2~p1这一段链表拿出来，放到head之前即可。
    另外，如果链表长度为n，且k>n，那么旋转k次就等价于旋转k-n次。
    """
    if not head or not head.next:
        return head
    p1, p2 = head, head
    # p1 先走k个位置
    n = 1
    for i in range(k):
        if p1.next:
            n += 1
            p1 = p1.next
        else:
            break
    if not p1.next: # 已经遍历到末尾
        p1 = head
        k = k % n
        if k == 0:
            return head
        for i in range(k):
            p1 = p1.next
            
    # p1和p2一起走k步
    while(p1.next):
        p1 = p1.next
        p2 = p2.next
    
    # p2~p1之间的子链表提到最前面
    p1.next = head
    head = p2.next
    p2.next = None
    
    return head

if '__main__' == __name__:
    l = ListNode([0,1,2])
    k = 2000000
    print(rotateRight(l, k).output())
        
    
    
    
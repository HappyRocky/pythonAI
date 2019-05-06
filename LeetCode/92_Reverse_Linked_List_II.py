# -*- coding: utf-8 -*-

"""
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

将一个链表的第m个到第n个节点之间的子链表进行反转。只能遍历一次。
备注：1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
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

def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    """
    定义两个指针p1和p2，p2始终落后
    """
    pre_head = ListNode(0)
    pre_head.next = head
    p1 = head
    p2 = pre_head
    count = 1 # p1的索引
    while(p1):
        if count == m: # 到达子链表的起始
            sub_head1, sub_head2 = p1, p2
            p1, p2 = p1.next, p2.next
        elif count > m and count <= n: # 需要让p1指向p2
            p_next = p1.next
            p1.next = p2
            p2 = p1
            p1= p_next
            if count == n: #到达子链表的末尾
                sub_head1.next = p1
                sub_head2.next = p2
                break
        else:
            p1, p2 = p1.next, p2.next
        count += 1
    return pre_head.next

if '__main__' == __name__:
    l = ListNode([1,2,3,4,5])
    m = 2
    n = 4
    print(reverseBetween(l, m ,n).output())
            
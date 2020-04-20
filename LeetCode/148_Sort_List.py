# -*- coding: utf-8 -*-

"""
Sort a linked list in O(n log n) time using constant space complexity.

将一个链表排序，时间复杂度为O(nlogn)，空间复杂度为O(1)

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
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
    
def sortList(head: ListNode) -> ListNode:
    """
    将链表转为数组，使用快速排序，然后再将数组转为链表
    """
    if not head:
        return head
    # 转为数组
    p = head
    node_list = []
    while(p):
        node_list.append(p)
        p = p.next
    # 快速排序
    def sort(l):
        """
        递归，快速排序
        """
        if len(l) <= 1:
            return
        key = l[0].val
        i, j = 0, len(l) - 1
        forward = 0 # 0是从右往左
        while(i < j):
            if forward == 0:
                if l[j].val < key:
                    l[i].val = l[j].val
                    forward = 1
                else:
                    j -= 1
            else:
                if l[i].val > key:
                    l[j].val = l[i].val
                    forward = 0
                else:
                    i += 1
        l[i].val = key
        sort(l[0:i])
        sort(l[i+1:])
    sort(node_list)
    return node_list[0]

def sortList2(head: ListNode) -> ListNode:
    """
    归并排序
    """
    def merge(h1, h2):
        """
        h1和h2都是排好序的链表。
        将两个链表归并排序，并返回新的链表。
        """
        pre = tail = ListNode(0)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
        tail.next = h1 or h2
        return pre.next
    
    # 递归结束条件
    if not head or not head.next:
        return head
    # 将链表对半分
    pre, slow, fast = None, head, head
    while fast and fast.next:
        pre, slow, fast = slow, slow.next, fast.next.next
    pre.next = None
    return merge(sortList2(head), sortList2(slow))

if '__main__' == __name__:
    head = ListNode([1,3,3,1,3,1,3,3,2,3,2,2,1,1,1])
    print(sortList(head).output())
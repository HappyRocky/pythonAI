# -*- coding: utf-8 -*-

'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

给定一个有序链表，将其中重复节点全部删除，只留下出现一次的节点。

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:
Input: 1->1->1->2->3
Output: 2->3
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
    与第83题相似，不同之处在于，83题是出现多次的节点只留下一个，而本题是出现多次的节点一个也不留。
    所以本题需要维护两个指针p1和p2，p1左边的始终是只出现过一次的，p2用来遍历。
    """
    if not head or not head.next:
        return head
    
    # 在head前追加一个节点
    p = ListNode(0)
    p.next = head
    p1, p2 = p, head
    # 开始遍历
    while(p2):
        # 判断p2及右邻是否相同，如果相同，则全部跳过
        if p2.next and p2.val == p2.next.val:
            v = p2.val
            while(p2 and p2.val == v):
                p2 = p2.next
        else: # 如果不同，则可以将p1指向p2，然后各进一步
            p1.next = p2
            p1 = p1.next
            p2 = p2.next
    p1.next = None
    return p.next

if '__main__' == __name__:
    head = ListNode([1,2,3,3,4,4,5,5])
    head = deleteDuplicates(head)
    print(head.output())
    
    

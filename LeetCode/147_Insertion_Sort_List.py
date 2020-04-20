# -*- coding: utf-8 -*-

"""
Sort a linked list using insertion sort.
A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list

对一个链表进行插入排序。
部分排好序的列表初始只包含第一个元素。
每次循环，一个元素从输入数据中移除，并插入到排好序的列表。

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
    
def insertionSortList(head: ListNode) -> ListNode:
    """
    插入排序，不占用额外空间。
    """
    if not head:
        return head
    end = head # 排好序的队列的最后一个节点
    while(end.next):
        # 将当前节点从队列中拿出来
        cur_node = end.next
        end.next = cur_node.next
        # 在排好序的队列中找到合适的位置
        p = ListNode(0)
        p1 = p
        p.next = head
        while(p != end):
            if cur_node.val < p.next.val:
                cur_node.next = p.next
                p.next = cur_node
                head = p1.next
                break
            p = p.next
        else: # 排好序的队列中没有当前节点的位置，放在最后
            cur_node.next = end.next
            end.next = cur_node
            end = end.next
    return head

if '__main__' == __name__:
    head = ListNode([6,1,3,2,5,4])
    print(insertionSortList(head).output())
            
                
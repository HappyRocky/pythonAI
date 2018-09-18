# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:19:38 2018

@author: gongyanshang1

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

合并 k 个有序链表，返回一个新链表。
分析复杂度。

示例：
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

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
    
    
def mergeKLists(lists):
    """
    :type lists: list[ListNode]
    :rtype: ListNode
    归并排序。
    维护 k 个指针，每次提取 k 个数中最小的数，然后此指针+1。
    使用了优先队列（最小堆），每次提取最小数的复杂度由O(k)变为了O(logk)。
    整体时间复杂度为O(nlogk)。
    """
    from queue import PriorityQueue
    
    # 初始化结果链表
    head = ListNode(0)
    p = head
    
    # 将每个链表的第一个节点放入到堆中
    q = PriorityQueue()
    for l in lists:
        if l:
            q.put((l.val, id(l), l))
            # 这里加上id(l)是因为元组比较大小是从左到右，如果l.val相等，则会继续比较第二个。
            # 如果此时第二个是l，则会报错，因为ListNode之间的大小不知道怎么比较
            # 而id(l)表示l的内存地址，int型，且可以保证所有存在对象的id都是不同的。
    
    # 每次从堆中选择最小节点
    while(not q.empty()):
        val, _, node = q.get()
        p.next = ListNode(val)
        p = p.next
        node = node.next
        if node:
            q.put((node.val, id(node), node))
    return head.next

if '__main__' == __name__:
    lists = []
    lists.append(ListNode([1,4,5]))
    lists.append(ListNode([1,3,4]))
    lists.append(ListNode([2,6]))
    print(mergeKLists(lists).output())
    
    
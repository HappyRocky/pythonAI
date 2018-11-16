# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:30:20 2018

@author: gongyanshang1

测试queue的四个队列
"""

from queue import Queue # last in last out
q = Queue()
q.put(1)
q.put(3)
q.put(2)
print(q.qsize())
print('LILO队列:', q.queue)
print('取出第一个:', q.get())
print('队列:', q.queue)


from queue import LifoQueue # last in first out，栈
q = LifoQueue()
q.put(1)
q.put(3)
q.put(2)
print('LifoQueue队列:', q.queue)
print('取出第一个:', q.get())
print('队列:', q.queue)

from queue import PriorityQueue # 优先队列，堆
q = PriorityQueue()
q.put((2, 'a')) # 元组比较大小是从左到右进行比较
q.put((3, 'b'))
q.put((1, 'c'))
print('优先队列:', q.queue)
print('依次取出:')
while(not q.empty()):
    print('', q.get())

from collections import deque # 双端队列
q = deque()
q.append(2)
q.append(3)
q.append(1)
print('双端队列:', q)
q.appendleft(4)
q.append(5)
print('左插4,右插5:', q)
q.rotate(2)
print('循环右移2次:', q)
print('取出最左端:', q.popleft())
print('取出最右端:', q.pop())
print('当前:', q)


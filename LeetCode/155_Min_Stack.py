# -*- coding: utf-8 -*-

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

设计一个栈，支持 push，pop，top 和在常数时间内将检索最小元素的功能。

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
class Node:
    def __init__(self, val, min, next):
        self.val = val
        self.min = min
        self.next = next
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None

    def push(self, x: int) -> None:
        if self.head:
            self.head = Node(x, min(self.head.min, x), self.head)
        else:
            self.head = Node(x, x, None)

    def pop(self) -> None:
        if self.head:
            self.head = self.head.next        

    def top(self) -> int:
        return self.head.val
        
    def getMin(self) -> int:
        return self.head.min
        
if '__main__' == __name__:
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-1)
    print(minStack.getMin()) 
    print(minStack.top())
    minStack.pop()
    print(minStack.getMin())  
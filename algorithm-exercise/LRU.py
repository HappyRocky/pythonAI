# -*- coding: utf-8 -*-
'''
实现LRU算法
Least Recently Used
首先要接收一个 capacity 参数作为缓存的最大容量，然后实现两个 API，一个是 put(key, val) 方法存入键值对，另一个是 get(key) 方法获取 key 对应的 val，如果 key 不存在则返回 -1。
注意哦，get 和 put 方法必须都是 O(1) 的时间复杂度
'''

class Node:
    '''
    节点类
    '''
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.child = None
        self.parent = None

class BiList:
    '''
    双向链表
    '''
    def __init__(self):
        self.top = Node(0, 0)
        self.tail = Node(0, 0)
        self.top.child = self.tail
        self.tail.parent = self.top
        self.size = 0

    def put(self, key, val):
        '''
        在top处新增一个节点
        :param val:
        :return:
        '''
        node = Node(key, val)
        node.child = self.top.child
        self.top.child = node
        node.child.parent = node
        node.parent = self.top
        self.size += 1
        return node

    def delete(self, node):
        '''
        删除node节点
        :param node:
        :return:
        '''
        node.parent.child = node.child
        node.child.parent = node.parent
        self.size -= 1
        del node

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = BiList()  # 存放 val
        self.map = dict()  # 存放 key 对应的 node

    def _delete(self, node):
        if node.key in self.map:
            self.cache.delete(node)
            del self.map[node.key]
            del node

    def put(self, key, val):
        if key in self.map: # 原来有这个key，则先删掉
            self._delete(self.map[key])
        if self.cache.size == self.cap: # 超出限制，则先删掉末尾节点
            self._delete(self.cache.tail.parent)
        self.map[key] = self.cache.put(key, val)

    def get(self, key):
        if key not in self.map:
            return None
        val = self.map[key].val
        self.put(key, val)
        return val

    def __str__(self):
        node = self.cache.top.child
        l = list()
        for _ in range(self.cache.size):
            l.append('{}:{}'.format(node.key, node.val))
            node = node.child
        return ', '.join(l)


if '__main__' == __name__:
    cache = LRUCache(3)
    cache.put('a', 1)
    cache.put('b', 2)
    cache.put('c', 3)
    print(cache)
    cache.put('d', 4)
    print(cache)
    cache.put('c', 4)
    print(cache)
    cache.get('d')
    print(cache)

# -*- coding: utf-8 -*-

"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. 
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
The cache is initialized with a positive capacity.
Follow up:
Could you do both operations in O(1) time complexity?

设计一个LRU缓存的数据结构。需要支持以下操作：get 和 put
get(key)：如果缓存中有key，则取出其value（总是正数），否则返回-1。
put(key,value)：设置key-value。如果缓存到达了容量上限，则应该先将最远使用的key删除，然后再插入新的值。

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
 
"""
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity # 设置容量
        self.oldest_key = None # 最久使用的key
        self.dict = dict() # <key,[value, time]>
        self.count = 0 # 自增
        
    def _update_oldest(self):
        """
        更新最老的key
        """
        self.oldest_key = min(self.dict, key=lambda x : self.dict[x][1]) if self.dict else None
    
    def _get_count(self):
        """
        获取当前时间的毫秒级时间戳
        """
        self.count += 1
        return self.count

    def get(self, key: int) -> int:
        """
        根据key获取value
        """
        if key not in self.dict:
            return -1
        values = self.dict[key]
        values[1] = self._get_count() # 更新时间戳
        if key == self.oldest_key: # 最老的key变成最近的key，需要重新计算最老的key
            self._update_oldest()
        return values[0]
            
    def put(self, key: int, value: int) -> None:
        """
        新增key
        """
        if key in self.dict: # 已有key，不用考虑删除的问题
            self.dict[key] = [value, self._get_count()]
            if key == self.oldest_key: # 更新最老key
                self._update_oldest()
        else: # 没有key，满了需要删除
            if len(self.dict) >= self.capacity:
                self.dict.pop(self.oldest_key)
                self._update_oldest()
            self.dict[key] = [value, self._get_count()]
        # 第一次put，初始化最老的key
        if not self.oldest_key:
            self.oldest_key = key
            
if '__main__' == __name__:
    cache = LRUCache(1)
    cache.put(2, 1)
    print(cache.get(2))       # returns 1
    cache.put(3, 2)    # evicts key 2
    print(cache.get(2))       # returns -1 (not found)
    print(cache.get(3))       # returns 3
    
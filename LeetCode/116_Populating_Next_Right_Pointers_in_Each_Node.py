# -*- coding: utf-8 -*-

"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

给定一个完美的二叉树，所有的叶节点都在同一个高度，每个非叶节点都有两个子节点。
将每个节点的next指向它的右边的节点，如果右边没有节点，则指向Null。
所有的next都初始化为Null。

Example:


Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
"""
class Node:
    def __init__(self, x):
        if isinstance(x, dict):
            self.val = x['v']
            self.left = Node(x['l']) if 'l' in x else None
            self.right = Node(x['r']) if 'r' in x else None
            self.next = None
        else:
            self.val = x
            self.left = None
            self.right = None
            self.next = None
    def show_next(self):
        """
        将每个节点的next打印出来
        """
        node_list = [root]
        i = 0
        while(i < len(node_list)):
            cur = node_list[i]
            if cur.left:
                node_list.append(cur.left)
            if cur.right:
                node_list.append(cur.right)
            i += 1
            if cur.next:
                print(f'{cur.val} -> {cur.next.val}')
            else:
                print(f'{cur.val} -> Null')
        

def connect(root: Node) -> Node:
    """
    将节点按照广度优先遍历，可以看出next的规律：
    2 -> 3
    4 -> 5 -> 6 -> 7
    8 -> ... -> 15
    转为序列的索引：
    0 -> null
    1 -> 2 -> null
    3 -> ... -> 6 -> null
    7 -> ... -> 14 -> null
    """
    if not root:
        return None
    # 广度优先遍历
    node_list = [root]
    i = 0
    while(i <len(node_list)):
        cur = node_list[i]
        if cur.left:
            node_list.append(cur.left)
        if cur.right:
            node_list.append(cur.right)
        i += 1
    # 赋值next
    root.next = None # 第一行只有一个根节点
    first_idx, last_idx = 1, 2 # 初始化第二行的起始索引和结束索引
    while(first_idx < len(node_list)):
        for i in range(first_idx, last_idx):
            node_list[i].next = node_list[i+1]
        node_list[last_idx].next = None
        # 更新到下一行
        first_idx = last_idx + 1
        last_idx = first_idx * 2
    return root
        
if '__main__' == __name__:
    root = Node({'v':1, 'l':{'v':2, 'l':4, 'r':5}, 'r':{'v':3, 'l':6, 'r':7}})
    connect(root).show_next()


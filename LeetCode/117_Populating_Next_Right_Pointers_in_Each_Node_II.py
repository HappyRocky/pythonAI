# -*- coding: utf-8 -*-

"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

给定一个二叉树。
将每个节点的next指向它的右边的节点，如果右边没有节点，则指向Null。
所有的next都初始化为Null。

Example:

Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}

Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
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
    将节点按照广度优先遍历，只要将同一层的节点区分出来即可。
    """
    if not root:
        return None
    # 广度优先遍历
    node_list = [(root, 0)]
    i = 0
    h = 0 # 深度
    while(i <len(node_list)):
        # 取出当前节点
        cur_node, cur_h = node_list[i]
        # 赋值next    
        if cur_h == h: # 与前一个节点位于同一层
            if i > 0:
                node_list[i-1][0].next = cur_node
        else: # 新的一层
            h = cur_h
        # 将子节点追加到列表中
        if cur_node.left:
            node_list.append((cur_node.left, h+1))
        if cur_node.right:
            node_list.append((cur_node.right, h+1))
        i += 1
    return root
        
if '__main__' == __name__:
    root = Node({'v':1, 'l':{'v':2, 'l':4, 'r':5}, 'r':{'v':3, 'l':6, 'r':7}})
    connect(root).show_next()
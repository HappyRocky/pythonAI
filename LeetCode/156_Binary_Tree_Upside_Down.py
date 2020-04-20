# -*- coding: utf-8 -*-

"""
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, 
flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

给定一个二叉树，所有的右节点或者为空，或者是叶子节点，且有一个左节点作为兄弟节点。
将二叉树上下倒置，其中原右节点抓换为左叶节点。
返回新的根。

For example:
Given a binary tree {1,2,3,4,5},
1
/ \
2 3
/ \
4 5

return the root of the binary tree [4,5,2,#,#,3,1].
4
/ \
5 2
  / \
 3 1
"""
class TreeNode:
    def __init__(self, x):
        if isinstance(x, dict):
            self.val = x['v']
            self.left = TreeNode(x['l']) if 'l' in x else None
            self.right = TreeNode(x['r']) if 'r' in x else None
        else:
            self.val = x
            self.left = None
            self.right = None
            
def upsideDownBinaryTree(root: TreeNode) -> TreeNode:
    """
    这棵树相当于一个链表，再加上某些节点可能会额外挂着一个右节点。
    所以可以使用链表反转的方法。
    """
    if not root or not root.left:
        return root
    # 反转
    p2 = root
    p1 = root.left
    while(p1):
        p1next = p1.left
        p1.right = p2
        p1.left = p2.right
        p2 = p1
        p1 = p1next
    return p2


        
    
    
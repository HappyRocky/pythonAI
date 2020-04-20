# -*- coding: utf-8 -*-

"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

给定一个二叉树，找到最小的深度。
最小深度指的是沿着从根节点到叶节点的最短路径的节点数。

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
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
            
def minDepth(root: TreeNode) -> int:
    """
    递归，寻找左子树和右子树的最小深度。
    """
    if not root:
        return 0
    d1 = minDepth(root.left)
    d2 = minDepth(root.right)
    return 1 + max(d1, d2) if d1 == 0 or d2 == 0 else 1 + min(d1, d2)

if '__main__' == __name__:
    r = TreeNode({'v':1,'l':{'v':2,'l':4,'r':5},'r':3})
    print(minDepth(r))
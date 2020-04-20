# -*- coding: utf-8 -*-

"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

给定一个二叉树，找到其最大深度。
最大深度是从根节点到叶节点的最长路径的节点数。
备注：一个叶节点指的是没有子节点的节点。

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
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
            
def maxDepth(root: TreeNode) -> int:
    """
    递归，寻找左子树和右子树的最大深度。
    """
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

if '__main__' == __name__:
    r = TreeNode({'v':1,'l':{'v':2,'l':4,'r':5},'r':3})
    print(maxDepth(r))
    
    
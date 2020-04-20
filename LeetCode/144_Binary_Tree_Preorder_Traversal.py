# -*- coding: utf-8 -*-

"""
Given a binary tree, return the preorder traversal of its nodes' values.

给定一个二叉树，返回前序遍历。

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,2,3]
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
            
def preorderTraversal(root: TreeNode) -> list:
    """
    前序遍历，迭代
    """
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right) if root else []
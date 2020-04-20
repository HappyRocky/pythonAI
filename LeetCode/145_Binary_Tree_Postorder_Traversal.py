# -*- coding: utf-8 -*-

"""
Given a binary tree, return the postorder traversal of its nodes' values.

给定一个二叉树，返回后续遍历的结果。

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [3,2,1]
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
            
def postorderTraversal(root: TreeNode) -> list:
    """
    递归，后续遍历
    """
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val] if root else []
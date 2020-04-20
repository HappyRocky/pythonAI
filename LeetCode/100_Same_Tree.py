# -*- coding: utf-8 -*-

"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

给定两个二叉树，判断两个树是否相同。
两个二叉树相同，指的是在结构上相同，且节点的值相同。

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
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
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    """
    递归，判断根节点、左子树、右子树是否分别相同。
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

if '__main__' == __name__:
    p = TreeNode({'v':1,'l':5,'r':{'v':7,'l':5,'r':8}})
    q = TreeNode({'v':1,'l':5,'r':{'v':7,'l':6,'r':8}})
    print(isSameTree(p,q))
# -*- coding: utf-8 -*-

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

给定一个二叉树，判断是否是一个镜像二叉树，即以它的中心进行轴对称。

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
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
def isSymmetric(root: TreeNode) -> bool:
    """
    判断左子树、右子树是否对称。
    """
    def fun(p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        return p is not None and q is not None and p.val == q.val and fun(p.left, q.right) and fun(p.right, q.left)
    return not root or fun(root.left, root.right)

if '__main__' == __name__:
    p = TreeNode({'v':1,'l':2,'r':2})
    print(isSymmetric(p))
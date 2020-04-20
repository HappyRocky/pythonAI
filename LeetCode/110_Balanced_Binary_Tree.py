# -*- coding: utf-8 -*-

"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

给定一个二叉树，判断是否是一个高度平衡树。
这个问题中，一个高度平衡的二叉树指的是二叉树的每个节点的两个子树的深度相差都不超过1。

Example 1:
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
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
    def to_dict(self):
        """
        将树用字典表示出来
        """
        if not self.left and not self.right:
            return self.val
        result = {'v':self.val}
        if self.left:
            result['l'] = self.left.to_dict()
        if self.right:
            result['r'] = self.right.to_dict()
        return result

def isBalanced(root: TreeNode) -> bool:
    """
    递归求取左右子树的高度，在递归过程中检验是否有任一节点的左右子树高度相差超过1。
    """
    def get_depth(root: TreeNode) -> (int, bool):
        """
        递归求取左右子树的高度，返回高度和左右子树相差是否超过1。
        """
        if not root:
            return 0, False
        depth1, is_over1 = get_depth(root.left)
        if is_over1:
            return 0, True
        depth2, is_over2 = get_depth(root.right)
        if is_over2 or abs(depth1 - depth2) > 1:
            return 0, True
        return 1 + max(depth1, depth2), False
    depth, is_over = get_depth(root)
    return not is_over

if '__main__' == __name__:
    root = TreeNode({'v': 0, 'l': {'v': -3, 'l': -10}, 'r': {'v': 9, 'l': 5}})
    print(isBalanced(root))
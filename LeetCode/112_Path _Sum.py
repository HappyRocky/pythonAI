# -*- coding: utf-8 -*-

"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.

给定一个二叉树和一个值 sum，判断这个树是否有一个从根到叶节点的路径，这个路径上所有节点值之和等于给定的值 sum。
备注：一个叶节点指的是没有子节点的节点。

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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
            
def hasPathSum(root: TreeNode, sum: int) -> bool:
    """
    递归，存在这种路径 <=> 存在左/右子树的一条路径上节点之和 + 根节点值 = sum
    """
    # 递归结束条件
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == sum
    return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)

if '__main__' == __name__:
    r = TreeNode({'v':1,'l':{'v':2,'l':4,'r':5},'r':3})
    print(hasPathSum(r, 7))
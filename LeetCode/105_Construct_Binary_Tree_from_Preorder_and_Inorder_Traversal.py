# -*- coding: utf-8 -*-

"""
Given preorder and inorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.

给定一棵树的前序遍历和中序遍历，构造这颗二叉树。

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
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
            
def buildTree(preorder: list, inorder: list) -> TreeNode:
    """
    根据前序和中序的根节点的位置不同，找到根节点、左子树和右子树的元素子序列。
    递归继续构建左子树和右子树。
    """
    # 递归结束条件
    if not preorder:
        return None
    # 先序遍历的第一个元素即为根节点
    root = TreeNode(preorder[0])
    idx = inorder.index(preorder[0]) # 中序遍历的根节点位置
    root.left = buildTree(preorder[1:idx+1], inorder[:idx])
    root.right = buildTree(preorder[idx+1:], inorder[idx+1:])
    return root

if '__main__' == __name__:
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    print(buildTree(preorder, inorder))
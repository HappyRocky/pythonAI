# -*- coding: utf-8 -*-
"""
Given inorder and postorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.

给定一棵树的中序遍历和后序遍历结果，构造这颗二叉树。
备注：
可以假设树中没有重复节点。

For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    
def buildTree(inorder: list, postorder: list) -> TreeNode:
    """
    中序为：左根右
    后序为：左右根
    后序确定根节点，然后中序确定左子树和右子树的元素子序列。
    递归继续构建左子树和右子树。
    """
    # 递归结束条件
    if not postorder:
        return None
    # 后序遍历的最后一个元素即为根节点
    root = TreeNode(postorder[-1])
    idx = inorder.index(postorder[-1]) # 中序遍历的根节点位置
    root.left = buildTree(inorder[:idx], postorder[:idx])
    root.right = buildTree(inorder[idx+1:], postorder[idx:-1])
    return root

if '__main__' == __name__:
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    print(buildTree(inorder, postorder).to_dict())

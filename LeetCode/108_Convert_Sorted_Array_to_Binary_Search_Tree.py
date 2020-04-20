# -*- coding: utf-8 -*-

"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

给定一个升序序列，将其转化为一个高度平衡的二叉搜索树。
这个问题中，一个高度平衡的二叉树指的是二叉树的每个节点的两个子树的深度相差都不超过1。

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
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
    
def sortedArrayToBST(nums: list) -> TreeNode:
    """
    如果左右两个子树的每个节点的左右子节点数都相差不超过1，则整体两个子树深度相差肯定也不超过1。
    而二叉搜索树要求左<根<右，因此根节点尽量从中间取，左部分为左子树，右部分为右子树。
    """
    # 递归结束条件
    if not nums:
        return None
    # 寻找根节点
    mid = int(len(nums) / 2)
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root

if '__main__' == __name__:
    nums = [-10,-3,0,5,9]
    print(sortedArrayToBST(nums).to_dict())
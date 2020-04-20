# -*- coding: utf-8 -*-

"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

给定一个二叉树，判断它是否是一个有效的二叉搜索树（BST）。
BST的定义：
一个节点的左子树的所有节点值都小于此节点值，右子树的所有节点值都大于此节点值。
左子树和右子树也都必须是二叉搜索树。
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
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
            
def isValidBST(root: TreeNode) -> bool:
    """
    递归，按照BST的定义判断。
    """
    def is_valid(tree: TreeNode, l, u):
        """
        判断是否tree的左节点值小于根节点、右节点大于根节点，且整个tree的每个节点的值在l和u之间
        """
        return tree is None or (tree.val > l and tree.val < u and is_valid(tree.left, l, tree.val) and is_valid(tree.right, tree.val, u))
    return is_valid(root, float('-inf'), float('inf'))

if '__main__' == __name__:
    root = TreeNode({'v':5,'l':1,'r':{'v':7,'l':6,'r':8}})
    print(isValidBST(root))
    
    
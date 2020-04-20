# -*- coding: utf-8 -*-

"""
给定先序遍历、中序遍历、后序遍历的其中两种遍历结果，构建一颗二叉树。
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
            
def buildTree(preorder: list, inorder: list) -> TreeNode:
    """
    根据前序和中序，确定二叉树。
    前序为：根左右
    中序为：左根右
    前序确定根节点，然后中序确定左子树和右子树的元素子序列。
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

def buildTree2(postorder: list, inorder: list) -> TreeNode:
    """
    根据中序和后序，确定二叉树。
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
    root.left = buildTree2(postorder[:idx], inorder[:idx])
    root.right = buildTree2(postorder[idx:-1], inorder[idx+1:])
    return root

def buildTree3(preorder: list, postorder: list) -> list:
    """
    根据前序和后序，确定二叉树。
    前序为：根左右
    后序为：左右根
    要比前两个函数复杂，因为无法将根节点作为左右子树的分界线。
    但是可以根据根节点一定是在两种序列的第一个和最后一个的特点，寻找到左右子树的界限。
    即：前序的左[0] = 后序的左[-1]
    但是有一点，如果前序的左右[0] = 后序的左右[-1]，那么说明只存在左子树或只存在右子树，这时会有多种构造结果。
    因此返回的不是一个树，而是数的序列。
    递归继续构建左子树和右子树。
    """
    # 递归结束条件
    if not preorder:
        return [None]
    if len(preorder) == 1:
        return [TreeNode(preorder[0])]
    # 寻找左右子树的界限
    result = []
    idx = postorder.index(preorder[1])
    left_tree_list = buildTree3(preorder[1:idx+2], postorder[:idx+1])
    right_tree_list = buildTree3(preorder[idx+2:], postorder[idx+1:-1])
    for left_tree in left_tree_list:
        for right_tree in right_tree_list:
            root = TreeNode(preorder[0])
            root.left = left_tree
            root.right = right_tree
            result.append(root)
    # 特殊：如果右子树为空，则也可以将左子树作为右子树，且左子树为空
    if idx == len(postorder) - 2:
        for left_tree in left_tree_list:
            root = TreeNode(preorder[0])
            root.left = None
            root.right = left_tree
            result.append(root)
    return result

if '__main__' == __name__:
    preorder = [0,1,2,3,4]
    inorder = [2,1,4,3,0]
    trees = buildTree3(preorder, inorder)
    for tree in trees:
        print(tree.to_dict())
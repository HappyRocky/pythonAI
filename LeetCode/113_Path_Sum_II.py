# -*- coding: utf-8 -*-

"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.

给定一个二叉树和一个值 sum，找到所有从根到叶节点的路径，每个路径上节点值之和等于 sum。

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
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
            
def pathSum(root: TreeNode, sum: int) -> list:
    """
    深度优先搜索，回溯法
    """
    if not root:
        return []
    def fun(root: TreeNode, sum:int, cur_list: list, result_list: list):
        """
        从root向下找到符合和等于sum的路径，追加到cur_list后，并把整个结果追加到结果list中。
        """
        # 到达叶节点
        if not root.left and not root.right:
            if sum == root.val:
                result_list.append(cur_list + [root.val])
        # 继续向下搜索
        else:
            if root.left:
                fun(root.left, sum - root.val, cur_list + [root.val], result_list)
            if root.right:
                fun(root.right, sum - root.val, cur_list + [root.val], result_list)
    
    result_list = []
    fun(root, sum, [], result_list)
    return result_list

if '__main__' == __name__:
    r = TreeNode({'v':1,'l':{'v':2,'l':4,'r':5},'r':3})
    print(pathSum(r, 7))
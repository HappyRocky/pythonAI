# -*- coding: utf-8 -*-

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

给定一个二叉树，按照层级顺序对节点进行遍历。

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
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
            
def levelOrder(root: TreeNode) -> list:
    """
    广度遍历
    """
    def fun(node_list):
        """
        递归，将node_list中的值按顺序提取出来，并追加他们的左右节点的值。
        """
        if not node_list:
            return []
        val_list = []
        new_node_list = []
        for node in node_list:
            val_list.append(node.val)
            if node.left:
                new_node_list.append(node.left)
            if node.right:
                new_node_list.append(node.right)
        return [val_list] + fun(new_node_list)
    
    return [] if not root else fun([root])

if '__main__' == __name__:
    r = TreeNode({'v':1,'l':5,'r':{'v':7,'l':5,'r':8}})
    print(levelOrder(r))
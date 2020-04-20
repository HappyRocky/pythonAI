# -*- coding: utf-8 -*-

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

给定一个二叉树，返回按照层级遍历节点的之字形顺序，即从左到右，然后在下一层从右到左，依次循环。

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    广度遍历，与第102相似，但是：
    1、需要将list变为stack，因为之字形正好符合后入先出。
    2、注意追加左右子树的顺序，先左后右和先右后左是交替进行的。
    """
    def fun(stack, order=0):
        """
        递归，将stack中的值按顺序提取出来，并追加他们的左右节点的值。
        """
        val_list = []
        new_stack = []
        while(stack):
            node = stack.pop()
            if not node:
                continue
            val_list.append(node.val)
            if order == 0:
                new_stack.extend([node.left, node.right])
            else:
                new_stack.extend([node.right, node.left])
        return [] if not val_list else [val_list] + fun(new_stack, 1 - order)
    return fun([root])

if '__main__' == __name__:
    r = TreeNode({'v':1,'l':{'v':2,'l':4,'r':5},'r':3})
    print(levelOrder(r))
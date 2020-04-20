# -*- coding: utf-8 -*-

"""
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

一个二叉搜索树（BST）的两个元素被错误地交换了。
修正此树，不能改变其结构。

Example 1:
Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
   
Example 2:
Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

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
            
def recoverTree(root: TreeNode) -> None:
    """
    中序遍历，左根右，将节点放到一个list中，将节点值放到一个list中，
    然后将节点值排序，依次放到节点中。
    """
    def in_order(node: TreeNode):
        """
        中序遍历，返回节点list和节点值list
        """
        if not node:
            return [], []
        left = in_order(node.left)
        mid = [node], [node.val]
        right = in_order(node.right)
        return left[0] + mid[0] + right[0], left[1] + mid[1] + right[1]
    node_list, val_list = in_order(root)
    val_sort_list = sorted(val_list)
    for i in range(len(node_list)):
        node_list[i].val = val_sort_list[i]
    
if '__main__' == __name__:
    root = TreeNode({'v':1,'l':5,'r':{'v':7,'l':6,'r':8}})
    recoverTree(root)
    print(root)
        
            
        
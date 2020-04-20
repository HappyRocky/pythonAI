# -*- coding: utf-8 -*-

"""
Given a binary tree, flatten it to a linked list in-place.

给定一个二叉树，将其转化为一个链表。

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
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
            
def flatten(root: TreeNode) -> None:
    """
    递归，构造链表
    """
    def fun(root: TreeNode) -> (TreeNode, TreeNode):
        """
        递归，构造链表：root -> fun(root.left) -> fun(root.right)
        """
        # 递归结束
        if not root.left and not root.right:
            return root, root
        # 左右子树构造链表
        head1, tail1, head2, tail2 = None, None, None, None
        if root.left:
            head1, tail1 = fun(root.left)
        if root.right:
            head2, tail2 = fun(root.right)
        # 串联起来：root -> head1 -> ... -> tail1 -> head2 -> ... -> tail2
        root.left = None
        if head1:
            root.right = head1
            if head2:
                tail1.right = head2
                return root, tail2
            return root, tail1
        else:
            root.right = head2
            return root, tail2
    if not root:
        return
    fun(root)

if '__main__' == __name__:
    r = TreeNode({'v':1,'l':{'v':2,'l':4,'r':5},'r':3})
    flatten(r)
    print(r.to_dict())
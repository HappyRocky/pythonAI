# -*- coding: utf-8 -*-

"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.

给定一个二叉树，只包含0-9的数字，每个从根节点到叶节点的路径都代表一个数字。
比如路径 1->2->3 代表数字 123。
找到所有根节点到叶节点路径所代表数字的和。
备注：一个叶节点是没有子节点的节点。

Example:
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
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
    
def sumNumbers(root: TreeNode) -> int:
    """
    深度优先遍历
    """
    if not root:
        return 0
    
    def fun(cur_sum, root, result):
        """
        对root进行深度优先遍历，结果加到cur_sum上，如果到了叶节点，则加到result上
        """
        cur_sum = cur_sum * 10 + root.val
        # 递归结束条件
        if not root.left and not root.right:
            result[0] += cur_sum
            return
        # 递归
        if root.left:
            fun(cur_sum, root.left, result)
        if root.right:
            fun(cur_sum, root.right, result)
    result = [0]
    fun(0, root, result)
    return result[0]
if '__main__' == __name__:
    r = TreeNode({'v':4, 'l':{'v': 9, 'l': 5, 'r': 1}, 'r':0})
    print(sumNumbers(r))
    
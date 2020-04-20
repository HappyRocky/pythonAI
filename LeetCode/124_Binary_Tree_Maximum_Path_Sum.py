# -*- coding: utf-8 -*-

"""
Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

给定一个非空的二叉树，找到最大路径和。
对于这个问题，一个路径指的是从一个起始节点通过任意父子连线到达另外一个节点的序列。
路径必须包含至少一个节点，且不必经过根节点。

Example 1:
Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
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
    
def maxPathSum(root: TreeNode) -> int:
    """
    双层分治法。
    对于根节点为root的二叉树，其最长路径是以下三者取最大（第一层分治）：
    1、root的左子树的最长路径
    2、root的右子树的最长路径
    3、经过root这个根节点的最长路径
    其中，前两者可以使用递归求出。
    第三者是以下两者相加，再加上根节点本身（第二层分治）：
    1、root的左子树的最长路径，且必须以root.left为起始点，路径可以为空
    2、root的右子树的最长路径，且必须以root.right为起始点，路径可以为空
    这两者都可以用递归求出。
    """
    def max_path_sum_from_root(root: TreeNode, memo: dict):
        """
        求root为根节点的二叉树的最长路径，且必须以根节点为起点，可以为空。
        结果肯定大于等于0。
        memo: {<root:max_sum>}，存放以某个节点最根节点的子树的最大路径，且必须以根节点为起点。
        """
        # 递归结束条件
        if not root:
            return 0
        if root in memo:
            return memo[root]
        # 开始递归
        left = max_path_sum_from_root(root.left, memo)
        right = max_path_sum_from_root(root.right, memo)
        result = max(max(left, right) + root.val, 0)
        memo[root] = result
        return result
        
    def max_path_sum(root: TreeNode, memo: dict):
        """
        求root为根节点的二叉树的最长路径。
        memo: {<root:max_sum>}，存放以某个节点最根节点的子树的最大路径，且必须以根节点为起点。
        """
        # 递归结束条件
        if not root:
            return -float('inf')
        # 外层分治
        left = max_path_sum(root.left, memo)
        right = max_path_sum(root.right, memo)
        mid = root.val + max_path_sum_from_root(root.left, memo) + max_path_sum_from_root(root.right, memo) # 内层分治
        return max(left, right, mid)
    return max_path_sum(root, dict())

def maxPathSum2(root: TreeNode) -> int:
    """
    将上述双层分治法进行改进。
    只保留内层分治，而外层分治可以根据内层分治的结果计算得到，即：
    对于根节点为root的二叉树，其最长路径是所有 （任选一个子树，经过这个子树的根节点的最长路径） 的最大值
    """
    def max_path_sum_from_root(root: TreeNode, max_sum):
        """
        求root为根节点的二叉树的最长路径，且必须以根节点为起点，可以为空。
        结果肯定大于等于0。
        max_sum: 存储所有（任选一个子树，经过这个子树的根节点的最长路径）的最大值
        """
        # 递归结束条件
        if not root:
            return 0
        # 开始递归
        left = max_path_sum_from_root(root.left, max_sum)
        right = max_path_sum_from_root(root.right, max_sum)
        # 更新max_sum
        max_sum[0] = max(max_sum[0], root.val + left + right)
        return max(max(left, right) + root.val, 0)
    max_sum = [-float('inf')]
    max_path_sum_from_root(root, max_sum)
    return max_sum[0]

if '__main__' == __name__:
    root = TreeNode({'v': 0, 'l': {'v': -3, 'l': -10}, 'r': {'v': 9, 'l': 5}})
    root = TreeNode(-3)
    print(maxPathSum2(root))
        
        
    
    
# -*- coding: utf-8 -*-

"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

给定一个整数n，产生所有不重复的二叉搜索树，元素为1...n。

Example:
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
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
    
def generateTrees(n: int) -> list:
    """
    递归，从待选列表中选出一个数，作为根节点，所有小于此数的作为左树，大于此数的作为右树。
    """
    def generate(l):
        """
        从l中依次选择一个数作为根节点，返回根节点列表。l为递增序列。
        """
        if not l:
            return [None]
        root_list = []
        for i in range(len(l)):
            left_trees = generate(l[:i])
            right_trees = generate(l[i+1:])
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(l[i])
                    root.left = left_tree
                    root.right = right_tree
                    root_list.append(root)
        return root_list
    return generate([x for x in range(1, n+1)])

if '__main__' == __name__:
    n = 0
    result = generateTrees(n)
    print(result)
            
        
        

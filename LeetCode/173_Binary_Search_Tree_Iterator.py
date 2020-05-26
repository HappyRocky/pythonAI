# -*- coding: utf-8 -*-
"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.

实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
调用 next() 将返回二叉搜索树中的下一个最小的数。

Note:
next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

备注：
next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数

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



class BSTIterator:

    def __init__(self, root: TreeNode):
        # 对二叉树进行排序，放到数组中
        self.index = -1
        self.sorted_list = self._sort(root)

    def _sort(self, node):
        """
        对node中的所有元素进行升序排序，返回排序数组
        :param node: 树节点
        :return:
        """
        if node is None:
            return []
        return self._sort(node.left) + [node.val] + self._sort(node.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            self.index += 1
            return self.sorted_list[self.index]
        return None

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index < len(self.sorted_list) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
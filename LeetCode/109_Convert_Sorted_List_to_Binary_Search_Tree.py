# -*- coding: utf-8 -*-

"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

给定一个升序单链表，将其转化为一个高度平衡的二叉搜索树。
这个问题中，一个高度平衡的二叉树指的是二叉树的每个节点的两个子树的深度相差都不超过1。

Example:
Given the sorted linked list: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
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

class ListNode:
    def __init__(self, x):
        
        if isinstance(x, list):
            self.val = x[0]
            self.next = None
            head = self
            for i in range(1, len(x)):
                head.next = ListNode(x[i])
                head = head.next
        else:
            self.val = x
            self.next = None
        
    def output(self):
        '''
        输出链表
        '''
        result = str(self.val)
        head = self.next
        while(head is not None):
            result += f' -> {head.val}'
            head = head.next
        return '(' + result + ')'
    
def sortedListToBST(head: ListNode) -> TreeNode:
    """
    将链表转为数组，然后使用第108题的方法：尽量对半分
    """
    # 转为数组
    nums = []
    while(head):
        nums.append(head.val)
        head = head.next
    def fun(nums):
        """
        将nums构造为BST，根节点位于nums最中央。
        """
        # 递归结束条件
        if not nums:
            return None
        # 寻找根节点
        mid = int(len(nums) / 2)
        root = TreeNode(nums[mid])
        root.left = fun(nums[:mid])
        root.right = fun(nums[mid+1:])
        return root

    return fun(nums)

if '__main__' == __name__:
    head = ListNode([-10,-3,0,5,9])
    print(sortedListToBST(head).to_dict())
    
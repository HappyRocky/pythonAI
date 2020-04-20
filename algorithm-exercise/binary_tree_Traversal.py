# -*- coding: utf-8 -*-

"""
研究二叉树的前序、中序、后续遍历，使用递归和非递归方法。
前序：根左右
中序：左根右
后续：左右根
前中后指的是“根”的位置。
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
        
def traversal(root: TreeNode, method=0) -> list:
    """
    递归
    root:根节点
    method: 0：前序遍历，1：中序遍历，2：后续遍历
    """
    if not root:
        return []
    mid = [root.val]
    left = traversal(root.left, method)
    right = traversal(root.right, method)
    if method == 0:
        return mid + left + right
    if method == 1:
        return left + mid + right
    return left + right + mid

def traversal2(root: TreeNode, method=0) -> list:
    """
    非递归，使用栈
    root:根节点
    method: 0：前序遍历，1：中序遍历，2：后续遍历
    """
    stack = list()
    stack.append(root)
    result = []
    while(stack):
        node = stack.pop() # node可能是两种类型，一种是节点值，一种是节点。
        if node:
            if isinstance(node, str):
                result.append(node)
            else:
                # 因为先进先出，所以按照倒序append到stack上
                next_list = [node.right, node.left]
                next_list.insert(2-method, node.val) 
                stack += next_list
    return result

if '__main__' == __name__:
    d = {'v':'A', 'l':{'v':'B','r':{'v':'C','l':'D'}}, 'r':{'v':'E', 'r':{'v':'F', 'l':{'v':'G', 'l':'H', 'r':'K'}}}}
    root = TreeNode(d)
    print(f'前序遍历：{traversal(root, 0)}')
    print(f'中序遍历：{traversal(root, 1)}')
    print(f'后序遍历：{traversal(root, 2)}')
    
    print(f'前序遍历：{traversal2(root, 0)}')
    print(f'前序遍历：{traversal2(root, 1)}')
    print(f'前序遍历：{traversal2(root, 2)}')
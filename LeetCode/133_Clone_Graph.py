# -*- coding: utf-8 -*-

"""
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. 
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

给定一个无向图的节点信息，返回这个图的深度拷贝。
图中的每个节点包含一个整数值和一个存放相邻节点的列表。

Example:
Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
 
Note:
The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
You must return the copy of the given node as a reference to the cloned graph.
"""
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
        
def cloneGraph(node: Node) -> Node:
    """
    深度优先遍历
    """
    if not node:
        return None
    
    def clone(node: Node, contain_dict):
        """
        递归，返回node的深度拷贝
        contain_dict存放已经扫描过的节点，防止重复递归。
        """
        # 拷贝当前节点
        new_node = Node(node.val, [])
        contain_dict[node] = new_node
        # 拷贝当前节点的邻居
        if not node.neighbors:
            return new_node
        new_neis = []
        for nei in node.neighbors:
            if nei in contain_dict:
                new_neis.append(contain_dict[nei])
            else:
                new_neis.append(clone(nei, contain_dict))
        new_node.neighbors = new_neis
        return new_node
    
    return clone(node, dict())

if '__main__' == __name__:
    node1 = Node(1, [])
    node2 = Node(2, [])
    node3 = Node(3, [])
    node4 = Node(4, [])
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    new_node1 = cloneGraph(node1)
    print(new_node1)
        
    
        
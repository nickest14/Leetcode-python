# 2196. Create Binary Tree From Descriptions

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        root: int = -1
        parent: dict = {}
        node: dict = {}

        for p, v, left in descriptions:
            if p not in node:
                node[p] = TreeNode(p)
                if p not in parent:
                    root = p
            if v not in node:
                node[v] = TreeNode(v)

            parent[v] = p
            if left:
                node[p].left = node[v]
            else:
                node[p].right = node[v]
        while root in parent:
            root = parent[root]

        return node[root]


Solution().createBinaryTree([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]])

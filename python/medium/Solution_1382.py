# 1382. Balance a Binary Search Tree

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode) -> List:
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)

        def build(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            m = (left + right) // 2
            root = TreeNode(nodes[m])
            root.left, root.right = build(left, m - 1), build(m + 1, right)
            return root

        nodes = dfs(root)
        return build(0, len(nodes) - 1)


root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
Solution().balanceBST(root)

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(4)
# root.right.left = TreeNode(3)
# Solution().balanceBST(root)

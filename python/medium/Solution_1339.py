# 1339. Maximum Product of Splitted Binary Tree

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod: int = 10**9 + 7
        self.best: int = 0

        def total_sum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)

        total = total_sum(root)

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            self.best = max(self.best, s * (total - s))
            return s

        dfs(root)
        return self.best % mod       


root = TreeNode(1)
root1 = TreeNode(2)
root2 = TreeNode(3)
root3 = TreeNode(4)
root4 = TreeNode(5)
root5 = TreeNode(6)
root.left = root1
root.right = root2
root.left.left = root3
root.left.right = root4
root.right.left = root5

ans = Solution().maxProduct(root)
print(ans)

# 102. Binary Tree Level Order Traversal

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, node: Optional[TreeNode], current_sum: int) -> int:
        if not node:
            return 0

        current_sum = current_sum * 2 + node.val

        if not node.left and not node.right:
            return current_sum

        leftSum = self.dfs(node.left, current_sum)
        rightSum = self.dfs(node.right, current_sum)

        return leftSum + rightSum

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)


root = TreeNode(1)
root1 = TreeNode(0)
root2 = TreeNode(1)
root3 = TreeNode(0)
root4 = TreeNode(1)
root5 = TreeNode(0)
root6 = TreeNode(1)
root.left = root1
root.right = root2
root1.left = root3
root1.right = root4
root2.left = root5
root2.right = root6

ans = Solution().sumRootToLeaf(root)
print(ans)

# 110. Balanced Binary Tree

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) > -1

    def height(self, root: Optional[TreeNode]):
        if root is None:
            return 0
        left_height, right_height = self.height(root.left), self.height(root.right)
        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

ans = Solution().isBalanced(root)
print(ans)

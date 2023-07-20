# 98. Validate Binary Search Tree

from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node: Optional[TreeNode], left: float, right: float):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float('-inf'), float('inf'))


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

ans = Solution().isValidBST(root)
print(ans)

#   2
#  / \
# 1   3
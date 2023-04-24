# 543. Diameter of Binary Tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> tuple:
            if not node:
                return 1, 0
            left, right = map(dfs, (node.left, node.right))
            current = left[1] + right[1] + 1
            max_so_far = max(left[0], right[0], current)
            max_ending_here = max(left[1], right[1]) + 1
            return max_so_far, max_ending_here

        max_length, _ = dfs(root)
        return max_length - 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
ans = Solution().diameterOfBinaryTree(root)
print(ans)

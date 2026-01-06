# 103. Binary Tree Zigzag Level Order Traversal

from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        values: list[int] = []
        queue: list[TreeNode] = [root]
        while queue:
            level_value: int = 0
            for _ in range(len(queue)):
                node = queue.pop(0)
                level_value += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            values.append(level_value)

        max_value = max(values)
        return values.index(max_value) + 1


root = TreeNode(1)
root1 = TreeNode(7)
root2 = TreeNode(0)
root3 = TreeNode(7)
root4 = TreeNode(-8)
root.left = root1
root.right = root2
root.left.left = root3
root.left.right = root4

ans = Solution().maxLevelSum(root)
print(ans)

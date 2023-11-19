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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque([root]) if root else []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level = reversed(level) if len(ans) % 2 else level
            ans.append(level)
        return ans


root = TreeNode(3)
root1 = TreeNode(9)
root2 = TreeNode(20)
root3 = TreeNode(15)
root4 = TreeNode(7)
root.left = root1
root.right = root2
root.right.left = root3
root.right.right = root4

ans = Solution().levelOrder(root)
print(ans)

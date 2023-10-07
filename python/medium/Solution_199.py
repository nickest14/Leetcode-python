# 199. Binary Tree Right Side View

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque([root])
        while q:
            right_side = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)
            if right_side:
                ans.append(right_side.val)

        return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.left.right = TreeNode(5)
ans = Solution().rightSideView(root)
print(ans)

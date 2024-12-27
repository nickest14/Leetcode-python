# 515. Find Largest Value in Each Tree Row

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans: list[int] = []
        queue: list[int] = [root]

        while queue:
            values: list[int] = []
            n: int = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(max(values))
        return ans


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

ans = Solution().largestValues(root)
print(ans)

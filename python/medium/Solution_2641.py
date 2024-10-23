# 2641. Cousins in Binary Tree II

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pq: deque[tuple[int, TreeNode]] = deque([(root.val, root)])
        while pq:
            n: int = len(pq)
            level_sum: int = 0
            for _, node in pq:
                level_sum += node.val

            for _ in range(n):
                local_sum, node = pq.popleft()
                child_sum: int = 0
                if node.left:
                    child_sum += node.left.val
                if node.right:
                    child_sum += node.right.val

                if node.left:
                    pq.append((child_sum, node.left))
                if node.right:
                    pq.append((child_sum, node.right))

                node.val = level_sum - local_sum

        return root


root: TreeNode = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(9)
root.left.left = TreeNode(1)
root.left.right = TreeNode(10)
root.right.right = TreeNode(7)
ans = Solution().replaceValueInTree(root)
print(ans)

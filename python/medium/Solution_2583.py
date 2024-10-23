# 2583. Kth Largest Sum in a Binary Tree

from collections import deque
from typing import Optional
import heapq


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        values: list[int] = []

        min_heap: list[int] = []
        q = deque([root])
        while q:
            level_value: int = 0
            for _ in range(len(q)):
                node: TreeNode = q.popleft()
                level_value += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            values.append(level_value)

            if len(min_heap) < k:
                heapq.heappush(min_heap, level_value)
            else:
                if level_value > min_heap[0]:
                    heapq.heapreplace(min_heap, level_value)

        return min_heap[0] if len(min_heap) == k else -1


root: TreeNode = TreeNode(5)
root.left = TreeNode(8)
root.right = TreeNode(9)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(6)
ans = Solution().kthLargestLevelSum(root, 2)
print(ans)

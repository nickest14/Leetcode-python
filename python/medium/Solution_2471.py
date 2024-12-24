# 2471. Minimum Number of Operations to Sort a Binary Tree by Level

from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        ans: int = 0
        queue: list[TreeNode] = [root]
        next_level: list[TreeNode] = []
        cur_values: list[tuple[int]] = []
        while queue:
            for i, node in enumerate(queue):
                cur_values.append((node.val, i))
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            idxs = [idx for _, idx in sorted(cur_values)]
            for i in range(len(idxs)):
                while i != idxs[i]:
                    j = idxs[i]
                    idxs[i], idxs[j] = idxs[j], idxs[i]
                    ans += 1

            queue = next_level
            next_level = []
            cur_values = []

        return ans


root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(3)
root.left.left = TreeNode(7)
root.left.right = TreeNode(6)
root.right.left = TreeNode(8)
root.right.right = TreeNode(5)
# root.right.right.left = TreeNode(10)
ans = Solution().minimumOperations(root)
print(ans)

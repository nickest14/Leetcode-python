# 1530. Number of Good Leaf Nodes Pairs

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count: int = 0
        max_distance: int = 10

        def dfs(node: TreeNode) -> List[int]:
            if not node:
                return [0] * (max_distance + 1)

            if not node.left and not node.right:
                ans = [0] * (max_distance + 1)
                ans[1] = 1
                return ans

            left = dfs(node.left)
            right = dfs(node.right)
            for i in range(1, distance + 1):
                for j in range(1, distance - i + 1):
                    self.count += left[i] * right[j]

            ans = [0] * (max_distance + 1)
            for i in range(1, max_distance):
                ans[i + 1] = left[i] + right[i]

            return ans

        dfs(root)
        return self.count


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
ans = Solution().countPairs(root, 3)
print(ans)

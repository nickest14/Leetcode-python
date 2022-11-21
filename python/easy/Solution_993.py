# 993. Cousins in Binary Tree

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(depth: int, node: TreeNode, parent: TreeNode, target: int):
            if node:
                if node.val == target:
                    return depth, parent
                return dfs(depth + 1, node.left, node, target) or dfs(depth + 1, node.right, node, target)
        dx, px = dfs(0, root, None, x)
        dy, py = dfs(0, root, None, y)
        return dx == dy and px is not py


t = TreeNode(1)
t_l = TreeNode(2)
t_r = TreeNode(3)
t_l_l = TreeNode(4)
t.left = t_l
t.right = t_r
t.left.left = t_l_l

ans = Solution().isCousins(t, 4, 3)
print(ans)

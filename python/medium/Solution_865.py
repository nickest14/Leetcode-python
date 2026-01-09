# 1339. Maximum Product of Splitted Binary Tree

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> tuple[int, Optional[TreeNode]]:
            if not node:
                return 0, None
                
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            if left_depth > right_depth:
                return (left_depth + 1, left_lca)            
            elif right_depth > left_depth:
                return (right_depth + 1, right_lca)
            else:
                return (left_depth + 1, node)

        return dfs(root)[1]


root = TreeNode(3)
root1 = TreeNode(5)
root2 = TreeNode(1)
root3 = TreeNode(6)
root4 = TreeNode(2)
root5 = TreeNode(6)
root6 = TreeNode(7)
root7 = TreeNode(4)
root.left = root1
root.right = root2
root.left.left = root3
root.left.right = root4
root.left.right.left = root6
root.left.right.right = root7

ans = Solution().subtreeWithAllDeepest(root)
print(ans)

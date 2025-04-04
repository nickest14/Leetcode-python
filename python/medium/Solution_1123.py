# 1123. Lowest Common Ancestor of Deepest Leaves

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode, depth: int) -> tuple[TreeNode, int]:
            if not node:
                return (None, depth)

            left_lca, left_depth = dfs(node.left, depth + 1)
            right_lca, right_depth = dfs(node.right, depth + 1)
            if left_depth > right_depth:
                return (left_lca, left_depth)            
            elif right_depth > left_depth:
                return (right_lca, right_depth)
            else:
                return (node, left_depth)

        lca_node, _ = dfs(root, 0)
        return lca_node


root = TreeNode(3)
root1 = TreeNode(5)
root2 = TreeNode(1)
root3 = TreeNode(6)
root4 = TreeNode(2)
root5 = TreeNode(0)
root6 = TreeNode(8)
root7 = TreeNode(7)
root8 = TreeNode(4)
root.left = root1
root.right = root2
root.left.left = root3
root.left.right = root4
root.right.left = root5
root.right.right = root6
root.left.right.left = root7
root.left.right.right = root8

ans = Solution().lcaDeepestLeaves(root)
print(ans.val)

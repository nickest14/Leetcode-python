# 2415. Reverse Odd Levels of Binary Tree

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(node1: Optional[TreeNode], node2: Optional[TreeNode], is_odd=False):
            if node1 is None or node2 is None:
                return
            if is_odd:
                node1.val, node2.val = node2.val, node1.val
            reverse(node1.left, node2.right, not is_odd)
            reverse(node1.right, node2.left, not is_odd)

        reverse(root.left, root.right, is_odd=True)
        return root


root = TreeNode(1)
root2 = TreeNode(2)
root3 = TreeNode(3)
root4 = TreeNode(4)
root5 = TreeNode(5)
root6 = TreeNode(6)
root7 = TreeNode(7)
root.left = root2
root.right = root3
root.left.left = root4
root.left.right = root5
root.right.left = root6
root.right.right = root7

ans = Solution().reverseOddLevels(root)
print(ans)

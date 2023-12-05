# 951. Flip Equivalent Binary Trees

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return not root1 and not root2
        if root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or\
            (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)

root2 = TreeNode(1)
root2.left = TreeNode(3)
root2.right = TreeNode(2)
root2.right.left = TreeNode(4)
ans = Solution().flipEquiv(root1, root2)
print(ans)

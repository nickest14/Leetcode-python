# 404. Sum of Left Leaves

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        while root:
            if child := root.left:
                while child.right and child.right is not root:
                    child = child.right
                if child.right:
                    child.right = None
                    root = root.right
                else:
                    left = root.left
                    if not left.left and not left.right:
                        ans += left.val
                    child.right = root
                    root = left
            else:
                root = root.right
        return ans


root = TreeNode(1)
root.left = TreeNode(9)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.left.right.right.left = TreeNode(10)
root.left.right.right.right = TreeNode(11)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
ans = Solution().sumOfLeftLeaves(root)
print(ans)

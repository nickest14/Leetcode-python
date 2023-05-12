# 783. Minimum Distance Between BST Nodes

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        stack, ans = [], float('inf')
        pre = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre is not None:
                ans = min(ans, abs(root.val - pre))
            pre = root.val
            root = root.right
        return ans


# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(6)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
root = TreeNode(27)
root.right = TreeNode(34)
root.right.right = TreeNode(58)
root.right.right.left = TreeNode(50)
root.right.right.left.left = TreeNode(44)
ans = Solution().minDiffInBST(root)
print(ans)

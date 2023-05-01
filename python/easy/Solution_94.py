# 94. Binary Tree Inorder Traversal

from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, ans = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)


ans = Solution().inorderTraversal(root)
print(ans)

#   1
#  / \
# 2   3
#    /
#   4

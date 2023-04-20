# 226. Invert Binary Tree

from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # iteration
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            queue += [node.left, node.right]
        return root

    # recursion
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if root:
    #         root.left, root.right = map(self.invertTree, (root.right, root.left))
    #     return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
ans = Solution().invertTree(root)
print(ans)

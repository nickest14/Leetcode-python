# 106. Construct Binary Tree from Inorder and Postorder Traversal

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {v: i for i, v in enumerate(inorder)}

        def helper(l: int, r: int):
            if l > r:
                return None

            root = TreeNode(postorder.pop())

            idx = inorder_idx.get(root.val)

            root.right = helper(idx + 1, r)
            root.left = helper(l, idx - 1)

            return root

        return helper(0, len(inorder) - 1)

    def buildTree2(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root = TreeNode(postorder.pop())

        idx = inorder.index(root.val)

        root.right = self.buildTree(inorder[idx + 1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)

        return root


inorder = [5, 9, 12, 3, 15, 20, 7]
postorder = [5, 12, 9, 15, 7, 20, 3]
ans = Solution().buildTree(inorder, postorder)
print(ans)

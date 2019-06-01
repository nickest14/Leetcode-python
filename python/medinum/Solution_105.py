# 105. Construct Binary Tree from Preorder and Inorder Traversal


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        index = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
ans = Solution().buildTree(preorder, inorder)
print(ans)

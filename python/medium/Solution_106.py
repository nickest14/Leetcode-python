# 106. Construct Binary Tree from Inorder and Postorder Traversal


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return root


inorder = [5, 9, 12, 3, 15, 20, 7]
postorder = [5, 12, 9, 15, 7, 20, 3]
ans = Solution().buildTree(inorder, postorder)
print(ans)

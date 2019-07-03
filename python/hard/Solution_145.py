# 145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = []

    def traversal(self, root): 
        if root.left:
            self.traversal(root.left)
        if root.right:
            self.traversal(root.right)
        self.ans.append(root.val)

    def postorderTraversal(self, root):
        if not root:
            return self.ans
        self.traversal(root)
        return self.ans


p = TreeNode(1)
p_2 = TreeNode(2)
p_3 = TreeNode(3)
p.right = p_2
p.right.left = p_3

ans = Solution().postorderTraversal(p)
print(ans)

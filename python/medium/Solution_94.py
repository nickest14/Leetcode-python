# 94. Binary Tree Inorder Traversal


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def addvalue(self, root, ans):
        if not root:
            return ans
        if root.left:
            ans = self.addvalue(root.left, ans)
        ans.append(root.val)
        if root.right:
            ans = self.addvalue(root.right, ans)
        return ans

    def inorderTraversal(self, root: TreeNode):
        ans = []
        if root:
            ans = self.addvalue(root, ans)
        return ans


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.right = node2
node2.left = node3

ans = Solution().inorderTraversal(node1)
print(ans)

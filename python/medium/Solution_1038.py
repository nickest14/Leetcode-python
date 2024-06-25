# 1038. Binary Search Tree to Greater Sum Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.dfs(root, 0)
        return root

    def dfs(self, node: TreeNode, sum):
        if node.right:
            sum = self.dfs(node.right, sum)

        sum += node.val
        node.val = sum

        if node.left:
            sum = self.dfs(node.left, sum)
        return sum


root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

ans = Solution().bstToGst(root)
print(ans.val)
print(ans.left.val)
print(ans.right.val)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ans = []

    def search(self, root):
        if root:
            self.ans.append(root.val)
            if root.left:
                self.search(root.left)
            if root.right:
                self.search(root.right)

    def preorderTraversal(self, root: TreeNode):
        if root:
            self.search(root)
        return self.ans


# root = TreeNode(1)
# root_left = TreeNode(2)
# root_right = TreeNode(3)
# root.left = root_left
# root.right = root_right

root = TreeNode(1)
root_l = TreeNode(2)
root_r_r = TreeNode(3)
root_r = TreeNode(4)
root.left = root_l
root.left.left = None
root.left.right = root_r_r
root.right = root_r

ans = Solution().preorderTraversal(None)
print(ans)

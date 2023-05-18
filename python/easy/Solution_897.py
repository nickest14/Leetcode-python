# 897. Increasing Order Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        prev = dummy = TreeNode(right=root)
        while root:
            if child := root.left:
                while child.right:
                    child = child.right
                child.right = root
                child = root.left
                root.left = None
                root = child
            else:
                prev.right = root
                prev = prev.right
                root = root.right
        return dummy.right


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)
ans = Solution().increasingBST(root)
print(ans)

# 104. Maximum Depth of Binary Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        nodelist = []
        nodelist.append(root)
        max_depth = 0
        while nodelist:
            temp_list = []
            max_depth += 1
            for i in nodelist:
                if i.left:
                    temp_list.append(i.left)
                if i.right:
                    temp_list.append(i.right)
            nodelist = temp_list
        return max_depth


root = TreeNode(3)
root1 = TreeNode(9)
root2 = TreeNode(20)
root3 = TreeNode(15)
root4 = TreeNode(7)
root.left = root1
root.right = root2
root.right.left = root3
root.right.right = root4

ans = Solution().maxDepth(root)
print(ans)

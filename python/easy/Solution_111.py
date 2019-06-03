# 111. Minimum Depth of Binary Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        level = 0
        if root:
            nodes = [root]
            while nodes:
                level += 1
                level_nodes = []
                for i in nodes:
                    if i.left or i.right:
                        if i.left:
                            level_nodes.append(i.left)
                        if i.right:
                            level_nodes.append(i.right)
                    else:
                        return level
                nodes = level_nodes
        return level


# [3, 9, 20, null, null, 15, 7]
t = TreeNode(3)
t_l = TreeNode(9)
t_r = TreeNode(20)
t_r_l = TreeNode(15)
t_r_r = TreeNode(7)
t.left = t_l
t.right = t_r
t.left.left = None
t.left.right = None
t.right.left = t_r_l
t.right.right = t_r_r

ans = Solution().minDepth(t)
print(ans)

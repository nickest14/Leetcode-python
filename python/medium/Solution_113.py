# 113. Path Sum II

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        if root.left is None and root.right is None and targetSum == root.val:
            return [[root.val]]
        l_path = self.pathSum(root.left, targetSum - root.val)
        r_path = self.pathSum(root.right, targetSum - root.val)
        left = [[root.val] + l_val for l_val in l_path]
        right = [[root.val] + r_val for r_val in r_path]
        return left + right


t = TreeNode(5)
t_l = TreeNode(4)
t_r = TreeNode(8)
t_l_l = TreeNode(11)
t_r_l = TreeNode(13)
t_r_r = TreeNode(4)
t.left = t_l
t.right = t_r
t.left.left = t_l_l
t.right.left = t_r_l
t.right.right = t_r_r

ans = Solution().pathSum(t, 20)
print(ans)

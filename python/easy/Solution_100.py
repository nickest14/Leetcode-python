# 100. Same Tree

from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) \
                and self.isSameTree(p.right, q.right)
        elif p or q:
            return False
        return True


p = TreeNode(1)
p_l = TreeNode(2)
p_r = TreeNode(3)
p.left = p_l
p.right = p_r

q = TreeNode(1)
q_l = TreeNode(2)
q_r = TreeNode(3)
q.left = q_l
q.right = q_r

ans = Solution().isSameTree(p, q)
print(ans)

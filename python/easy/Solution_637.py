# 637. Average of Levels in Binary Tree

from typing import List, Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        queue = collections.deque([root])
        while queue:
            val = 0
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                val += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(val/n)
        return ans


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

ans = Solution().averageOfLevels(t)
print(ans)

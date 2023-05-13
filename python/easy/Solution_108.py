# 108. Convert Sorted Array to Binary Search Tree

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left: int, right: int):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(nums) - 1)


nums = [-10, -3, 0, 5, 9]
ans = Solution().sortedArrayToBST(nums)
print(ans)

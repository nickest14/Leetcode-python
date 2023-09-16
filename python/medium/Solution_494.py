# 494. Target Sum

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> number of different expressions

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])
            return dp[(i, total)]

        return backtrack(0, 0)


ans = Solution().findTargetSumWays([1, 1, 1, 1, 1], 3)

print(ans)

# 416. Partition Equal Subset Sum

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum: int = sum(nums)
        if total_sum % 2 != 0:
            return False

        target: int = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]


ans = Solution().canPartition([1, 5, 11, 5])
print(ans)

# 377. Combination Sum IV

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # bottom up dp
        dp = {0: 1}

        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n, 0)
        return dp[target]


ans = Solution().combinationSum4([1, 2, 3], 4)
print(ans)

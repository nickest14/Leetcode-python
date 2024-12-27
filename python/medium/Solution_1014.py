# 1014. Best Sightseeing Pair

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans: int = 0
        dp: list[int] = [0] * len(values)
        dp[0] = values[0]

        for i in range(1, len(values)):
            dp[i] = max(dp[i - 1], values[i - 1] + i - 1)
            ans = max(ans, dp[i] + values[i] - i)

        return ans


ans = Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6])
print(ans)

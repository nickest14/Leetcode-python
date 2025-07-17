# 3202. Find the Maximum Length of Valid Subsequence II

from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n: int = len(nums)
        if n < 2:
            return 0

        dp: list[dict[int, int]] = [{} for _ in range(n)]
        ans: int = 0

        for i in range(n):
            for j in range(i):
                mod: int = (nums[i] + nums[j]) % k
                if mod in dp[j]:
                    dp[i][mod] = max(dp[i].get(mod, 0), dp[j][mod] + 1)
                else:
                    dp[i][mod] = max(dp[i].get(mod, 0), 2)

                ans = max(ans, dp[i][mod])

        return ans


ans = Solution().maximumLength([1, 2, 3, 4, 5], 2)
print(ans)

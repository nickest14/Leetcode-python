# 1262. Greatest Sum Divisible by Three

from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp: list[int] = [0, float("-inf"), float("-inf")]
        for num in nums:
            tmp: list[int] = dp[:]
            for r in range(3):
                new_r: int = (r + num) % 3
                tmp[new_r] = max(tmp[new_r], dp[r] + num)
            dp = tmp
        return dp[0]


ans = Solution().maxSumDivThree([3, 6, 5, 1, 8])
print(ans)

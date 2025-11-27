# 3381. Maximum Subarray Sum With Length Divisible by K

from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        inf: int = float("inf")
        min_prefix: list[int] = [inf] * k
        min_prefix[0] = 0

        prefix: int = 0
        ans: int = float("-inf")

        for i, x in enumerate(nums):
            prefix += x
            mod: int = (i + 1) % k

            if min_prefix[mod] != inf:
                ans = max(ans, prefix - min_prefix[mod])

            min_prefix[mod] = min(min_prefix[mod], prefix)

        return ans


ans = Solution().maxSubarraySum([-1, -2, -3, -4, -5], 4)
print(ans)

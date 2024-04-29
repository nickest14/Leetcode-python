# 209. Minimum Size Subarray Sum

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        l, total = 0, 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                ans = min(ans, r - l + 1)
                total -= nums[l]
                l += 1

        return ans if ans != float('inf') else 0


ans = Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
print(ans)

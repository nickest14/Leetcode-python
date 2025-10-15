# 3350. Adjacent Increasing Subarrays Detection II

from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n: int = len(nums)
        ans: int = 0
        inc, prev_inc, = 1, 0
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc += 1
            else:
                prev_inc = inc
                inc = 1
            half = inc >> 1
            m = min(prev_inc, inc)
            candidate = max(half, m)
            if candidate > ans:
                ans = candidate

        return ans


ans = Solution().maxIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1])
print(ans)

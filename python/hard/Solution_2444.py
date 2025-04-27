# 2444. Count Subarrays With Fixed Bounds

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans: int = 0
        prev_min = prev_max = bad = -1

        for i, num in enumerate(nums):
            if num == minK:
                prev_min = i
            if num == maxK:
                prev_max = i
            if num < minK or num > maxK:
                bad = i
            if prev_min != -1 and prev_max != -1:
                ans += max(0, min(prev_min, prev_max) - bad)

        return ans


# ans = Solution().countSubarrays([1, 3, 5, 2, 7, 5], 1, 5)
ans = Solution().countSubarrays([1, 1, 2, 3, 5], 1, 5)
print(ans)

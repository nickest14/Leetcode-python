# 3634. Minimum Removals to Balance Array

from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        if nums[0] * k >= nums[-1]:
            return 0

        n: int = len(nums)
        left: int = 0
        ans = n
        for right, num in enumerate(nums):
            while left < right and nums[left] * k < num:
                left += 1
            ans = min(ans, n - right + left - 1)

        return ans


ans = Solution().minRemoval([2, 1, 5], 2)
print(ans)

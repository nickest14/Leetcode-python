# 3423. Maximum Difference Between Adjacent Elements in a Circular Array

from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n: int = len(nums)
        max_diff: int = max(abs(nums[i] - nums[i + 1]) for i in range(n - 1))
        return max(max_diff, abs(nums[0] - nums[-1]))


ans = Solution().maxAdjacentDistance([1, 2, 4])
print(ans)

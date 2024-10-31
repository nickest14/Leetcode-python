# 1671. Minimum Number of Removals to Make Mountain Array

from bisect import bisect_left
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        size: int = len(nums)

        dp: list[int] = []
        left: list[int] = [0] * size
        for i in range(size):
            idx: int = bisect_left(dp, nums[i])
            if idx == len(dp):
                dp.append(nums[i])
            else:
                dp[idx] = nums[i]
            left[i] = len(dp)

        dp: list[int] = []
        right: list[int] = [0] * size
        for j in range(size - 1, -1, -1):
            idx = bisect_left(dp, nums[j])
            if idx == len(dp):
                dp.append(nums[j])
            else:
                dp[idx] = nums[j]
            right[j] = len(dp)

        ans: int = size
        for i in range(size):
            if left[i] > 1 and right[i] > 1:
                ans = min(ans, size - left[i] - right[i] + 1)

        return ans


ans = Solution().minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1])
# ans = Solution().minimumMountainRemovals([1, 3, 6, 9, 12, 11, 10, 2])
# ans = Solution().minimumMountainRemovals([1, 3, 5, 2, 4, 6, 8, 10, 1])
print(ans)
# 2563. Count the Number of Fair Pairs

from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans: int = 0
        for i in range(len(nums) - 1, -1, -1):
            val = nums[i]
            left = bisect_left(nums, lower - val, lo=0, hi=i)
            right = bisect_right(nums, upper - val, lo=0, hi=i)
            ans += right - left
        return ans


ans = Solution().countFairPairs([0, 1, 7, 4, 4, 5], 3, 6)
# ans = Solution().countFairPairs([1, 2, 4, 6, 8, 13], 10, 13)
print(ans)

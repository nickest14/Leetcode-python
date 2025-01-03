# 2270. Number of Ways to Split Array

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total: int = sum(nums)
        accumulate: int = 0

        ans: int = 0
        for _, num in enumerate(nums[:-1]):
            accumulate += num
            if 2 * accumulate >= total:
                ans += 1
        return ans


ans = Solution().waysToSplitArray([10, 4, -8, 7])
print(ans)

# 1749. Maximum Absolute Sum of Any Subarray

from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        sum, min_sum, max_sum = 0, 0, 0
        for num in nums:
            sum += num
            max_sum = max(max_sum, sum)
            min_sum = min(min_sum, sum)
        return abs(max_sum - min_sum)


ans = Solution().maxAbsoluteSum([1, -3, 2, 3, -4])
print(ans)

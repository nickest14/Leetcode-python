# 724. Find Pivot Index

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for ind, val in enumerate(nums):
            right -= val
            if left == right:
                return ind
            left += val
        return -1


ans = Solution().pivotIndex([1, 7, 3, 6, 5, 6])
print(ans)

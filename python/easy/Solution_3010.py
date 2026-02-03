# 3010. Divide an Array Into Subarrays With Minimum Cost I

from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first: int = nums[0]
        sorted_nums: List[int] = sorted(nums[1:])

        return first + sorted_nums[0] + sorted_nums[1]


ans = Solution().minimumCost([1, 2, 3, 12])
print(ans)

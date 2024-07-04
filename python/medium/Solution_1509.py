# 1509. Minimum Difference Between Largest and Smallest Value in Three Moves

from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 4:
            return 0

        nums.sort()

        return min(
            nums[length - 4] - nums[0],
            nums[length - 3] - nums[1],
            nums[length - 2] - nums[2],
            nums[length - 1] - nums[3]
        )


ans = Solution().minDifference([1, 5, 0, 10, 14])
print(ans)

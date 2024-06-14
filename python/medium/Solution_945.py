# 945. Minimum Increment to Make Array Unique

from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                ans += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
        return ans


ans = Solution().minIncrementForUnique([3, 2, 1, 2, 1, 7])
print(ans)

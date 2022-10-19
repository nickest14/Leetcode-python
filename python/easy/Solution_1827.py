# 1827. Minimum Operations to Make the Array Increasing

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for ind in range(1, len(nums)):
            if nums[ind] <= nums[ind - 1]:
                ans += nums[ind - 1] - nums[ind] + 1
                nums[ind] = nums[ind - 1] + 1
        return ans


nums = [1, 1, 1]
ans = Solution().minOperations(nums)
print(ans)

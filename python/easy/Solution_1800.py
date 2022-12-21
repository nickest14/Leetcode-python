# 1800. Maximum Ascending Subarray Sum

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans, curr = 0, 0
        for ind, num in enumerate(nums):
            if ind == 0 or nums[ind - 1] >= num:
                curr = 0
            curr += num
            ans = max(ans, curr)
        return ans


ans = Solution().maxAscendingSum([10, 20, 30, 5, 10, 50])
print(ans)

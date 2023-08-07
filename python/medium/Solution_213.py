# 213. House Robber II

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
        prev_max, cur_max = 0, 0
        for n in nums:
            temp = max(n + prev_max, cur_max)
            prev_max = cur_max
            cur_max = temp
        return cur_max


ans = Solution().rob([1, 2, 3, 1])
print(ans)

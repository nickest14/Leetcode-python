# 1888. Minimum Number of Flips to Make the Binary String Alternating

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans: int = nums[0] + nums[-1]
        for i in range(1, len(nums) // 2):
            ans = max(ans, nums[i] + nums[-1 - i])
        return ans


ans = Solution().minPairSum([3, 5, 4, 2, 4, 6])
print(ans)

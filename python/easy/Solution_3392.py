# 3392. Count Subarrays of Length Three With a Condition

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans: int = 0
        for i in range(1, len(nums) - 1):
            ans += 1 if (nums[i - 1] + nums[i + 1]) * 2 == nums[i] else 0
        return ans


ans = Solution().countSubarrays([1, 2, 1, 4, 1])
print(ans)

# 2210. Count Hills and Valleys in an Array

from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans: int = 0
        left: int = 0
        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i + 1]:
                if (nums[left] < nums[i] and nums[i] > nums[i + 1]) or (
                    nums[left] > nums[i] and nums[i] < nums[i + 1]
                ):
                    ans += 1
                left = i
        return ans


ans = Solution().countHillValley([2, 4, 1, 1, 6, 5])
print(ans)

# 448. Find All Numbers Disappeared in an Array

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])
        return [i + 1 for i, num in enumerate(nums) if num > 0]


ans = Solution().findDisappearedNumbers([4, 5, 1, 1, 2])
print(ans)

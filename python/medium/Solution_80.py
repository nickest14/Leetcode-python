# 80. Remove Duplicates from Sorted Array II

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1
            for _ in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l


ans = Solution().removeDuplicates([2, 7, 7, 7, 7, 11, 15])
print(ans)

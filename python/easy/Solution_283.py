# 283. Move Zeroes

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j, num in enumerate(nums):
            if num != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1


# nums = [0, 1, 0, 3, 12]
nums = [0, 0, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)

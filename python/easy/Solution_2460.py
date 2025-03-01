# 2460. Apply Operations to an Array

from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        non_zero_index: int = 0
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        for i in range(non_zero_index, n):
            nums[i] = 0

        return nums


ans = Solution().applyOperations([1, 2, 2, 1, 1, 0])
print(ans)

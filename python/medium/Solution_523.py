# 523. Continuous Subarray Sum

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}
        total = 0
        for i, j in enumerate(nums):
            total += j
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        return False


nums = [23, 2, 6, 4, 7]
k = 6
ans = Solution().checkSubarraySum(nums, k)
print(ans)

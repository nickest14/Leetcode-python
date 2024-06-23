# 3192. Minimum Operations to Make Binary Array Elements Equal to One II

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        flip = 0

        for i in range(len(nums)):
            if nums[i] == flip:
                ans += 1
                flip = 1 - flip

        return ans

    # # Timeout solution
    # def minOperations(self, nums: List[int]) -> int:
    #     ans = 0
    #     left, right = 0, len(nums)
    #     while left < right and not all(nums):
    #         for i in range(left, right):
    #             if nums[i] == 0:
    #                 ans += 1
    #                 left = i + 1
    #                 for j in range(i, right):
    #                     nums[j] = 1 if nums[j] == 0 else 0
    #                 break

    #     return ans


ans = Solution().minOperations([0, 1, 1, 0, 1])
# ans = Solution().minOperations([0, 1, 0, 1, 0, 1])
print(ans)

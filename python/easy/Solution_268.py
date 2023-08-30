# 268. Missing Number

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)

        for i in range(len(nums)):
            ans += i - nums[i]
        return ans

    # Another solutionans
    # def missingNumber(self, nums: List[int]) -> int:
    #     length = len(nums)
    #     return (length + 1) * length // 2 - sum(nums)


ans = Solution().missingNumber([1, 3, 5, 2, 0])
print(ans)

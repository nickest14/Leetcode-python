# 2221. Find Triangular Sum of an Array

from typing import List
from math import comb


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n: int = len(nums)
        ans = 0

        for i in range(n):
            ans = (ans + comb(n - 1, i) * nums[i]) % 10

        return ans


ans = Solution().triangularSum([1, 2, 3, 4, 5])
print(ans)

# 3190. Find Minimum Operations to Make All Elements Divisible by Three

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if num % 3 != 0:
                ans += 1

        return ans


ans = Solution().minimumOperations([1, 2, 3, 4])
print(ans)

# 3512. Minimum Operations to Make Array Sum Divisible by K

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k


ans = Solution().minOperations([3, 9, 7], 5)
print(ans)

# 1785. Minimum Elements to Add to Form a Given Sum

from typing import List
import math


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return math.ceil(abs(goal - sum(nums)) / limit)


nums = [1, -1, 1]
limit = 3
goal = -4
ans = Solution().minElements(nums, limit, goal)
print(ans)

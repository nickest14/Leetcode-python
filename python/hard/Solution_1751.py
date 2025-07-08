# 1751. Maximum Number of Events That Can Be Attended II

from bisect import bisect_left
from typing import List
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def binary_search(self, i: int) -> int:
        return bisect_left(self.events, self.events[i][1] + 1, key=lambda e : e[0])

    @lru_cache(maxsize=None)
    def dp(self, i: int, k: int) -> int:
        if i >= len(self.events) or k <= 0:
            return 0
        
        skip_value: int = self.dp(i + 1, k)
        next: int = self.binary_search(i)
        take_value: int = self.events[i][2] + self.dp(next, k - 1)
        return max(skip_value, take_value)

    def maxValue(self, events: List[List[int]], k: int) -> int:
        self.events = sorted(events)
        return self.dp(0, k)


ans = Solution().maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2)
print(ans)

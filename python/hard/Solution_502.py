# 502. IPO

from typing import List
from heapq import heappush, heappop


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        max_heap = []
        i = 0
        n = len(profits)
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heappush(max_heap, -projects[i][1])
                i += 1
            if not max_heap:
                break
            w += -heappop(max_heap)

        return w


k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
ans = Solution().findMaximizedCapital(k, w, profits, capital)
print(ans)

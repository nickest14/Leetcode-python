# 2940. Find Building Where Alice and Bob Can Meets

from typing import List
import heapq


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n: int = len(heights)
        q: int = len(queries)
        ans: list[int] = [-1] * q
        deferred: list[list[int]] = [[] for _ in range(n)]
        pq: list[tuple[int]] = []

        for i, q in enumerate(queries):
            alice, bob = q[0], q[1]
            if alice > bob:
                alice, bob = bob, alice
            if alice == bob or heights[alice] < heights[bob]:
                ans[i] = bob
            else:
                deferred[bob].append((heights[alice], i))

        for i in range(n):
            for q in deferred[i]:
                heapq.heappush(pq, q)
            while pq and pq[0][0] < heights[i]:
                ans[pq[0][1]] = i
                heapq.heappop(pq)

        return ans


ans = Solution().leftmostBuildingQueries([6, 4, 8, 5, 2, 7], [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]])
print(ans)

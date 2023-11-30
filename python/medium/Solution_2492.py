# 2492. Minimum Score of a Path Between Two Cities

from typing import List
from collections import defaultdict


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst, dist in roads:
            adj[src].append((dst, dist))
            adj[dst].append((src, dist))

        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            nonlocal ans
            for nei, dist in adj[i]:
                ans = min(ans, dist)
                dfs(nei)

        ans = float('inf')
        visit = set()
        dfs(1)
        return ans


ans = Solution().minScore(4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]])
print(ans)

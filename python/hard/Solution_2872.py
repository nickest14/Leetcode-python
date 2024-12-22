# 2872. Maximum Number of K-Divisible Components

from typing import List
from collections import defaultdict


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj: dict[int, List[int]] = defaultdict(list)
        visited = set()
        ans: int = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node: int):
            nonlocal ans
            leaf: int = values[node]
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    leaf += dfs(neighbor)
            if leaf % k == 0:
                ans += 1
                leaf = 0
            return leaf

        dfs(0)

        return max(ans, 1)


ans = Solution().maxKDivisibleComponents(5, [[0, 2], [1, 2], [1, 3], [2, 4]], [3, 0, 6, 1, 5, 2, 1], 3)
print(ans)

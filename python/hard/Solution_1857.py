# 1857. Largest Color Value in a Directed Graph

from typing import List
from collections import deque

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n: int = len(colors)
        adj: List[List[int]] = [[] for _ in range(n)]
        indegree: List[int] = [0] * n

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        dp = [[0] * 26 for _ in range(n)]
        queue: deque[int] = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
            dp[i][ord(colors[i]) - ord('a')] = 1

        visited: int = 0
        max_color: int = 0

        while queue:
            node = queue.popleft()
            visited += 1

            for neighbor in adj[node]:
                for c in range(26):
                    inc = 1 if ord(colors[neighbor]) - ord('a') == c else 0
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c] + inc)

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

            max_color = max(max_color, max(dp[node]))

        return max_color if visited == n else -1        


ans = Solution().largestPathValue("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]])
print(ans)

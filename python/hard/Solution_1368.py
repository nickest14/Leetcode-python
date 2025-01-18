# 1368. Minimum Cost to Make at Least One Valid Path in a Grid

from typing import List
from collections import deque


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        min_cost: list[list[int]] = [[float("inf")] * n for _ in range(m)]
        min_cost[0][0] = 0

        q: deque[tuple[int, int]] = deque([(0, 0)])
        directions: list[tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            r, c = q.popleft()
            for i, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc
                cost = 1 if grid[r][c] != i + 1 else 0
                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and min_cost[r][c] + cost < min_cost[nr][nc]
                ):
                    min_cost[nr][nc] = min_cost[r][c] + cost

                    if cost == 1:
                        q.append((nr, nc))
                    else:
                        q.appendleft((nr, nc))
        return min_cost[m - 1][n - 1]


ans = Solution().minCost([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]])
print(ans)

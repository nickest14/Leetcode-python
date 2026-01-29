# 3651. Minimum Cost to Make at Least One Valid Path in a Grid

from typing import List
from heapq import heappop, heappush


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        available: list[list[tuple[int, int, int]]] = [
            sorted(
                [
                    (grid[i][j], i, j)
                    for i in range(len(grid))
                    for j in range(len(grid[0]))
                ],
                reverse=True,
            )
            for _ in range(k)
        ]
        visited: list[list[int]] = [
            [11 for i in range(len(grid[0]))] for j in range(len(grid))
        ]

        heap: list[tuple[int, int, int, int]] = [(0, 0, 0, 0)]  # cost, x, y, teleports
        while heap:
            cost, x, y, tps = heappop(heap)
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return cost
            if visited[x][y] <= tps:
                continue
            visited[x][y] = tps
            if x + 1 < len(grid):
                heappush(heap, (cost + grid[x + 1][y], x + 1, y, tps))
            if y + 1 < len(grid[0]):
                heappush(heap, (cost + grid[x][y + 1], x, y + 1, tps))
            while tps < k and available[tps] and available[tps][-1][0] <= grid[x][y]:
                _, x1, y1 = available[tps].pop()
                heappush(heap, (cost, x1, y1, tps + 1))


ans = Solution().minCost([[1, 3, 3], [2, 5, 4], [4, 3, 5]], 2)
print(ans)

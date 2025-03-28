# 2503. Maximum Number of Points From Grid Queries

from typing import List
import heapq


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * cols for _ in range(rows)]
        visited[0][0] = True

        heap: list[tuple[int, int, int]] = []
        heapq.heappush(heap, (grid[0][0], 0, 0))

        points: int = 0
        ans = [0] * len(queries)

        sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])
        for query_val, query_idx in sorted_queries:
            while heap and heap[0][0] < query_val:
                _, row, col = heapq.heappop(heap)
                points += 1
                for dx, dy in directions:
                    nx, ny = row + dx, col + dy
                    if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                        visited[nx][ny] = True
                        heapq.heappush(heap, (grid[nx][ny], nx, ny))
            ans[query_idx] = points
        return ans


ans = Solution().maxPoints([[1, 2, 3], [2, 5, 7], [3, 5, 1]], [5, 6, 2])
print(ans)

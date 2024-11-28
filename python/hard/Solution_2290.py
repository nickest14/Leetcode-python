# 2290. Minimum Obstacle Removal to Reach Corner

from typing import List
from collections import deque


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions: list[tuple[int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque([(0, 0, 0)])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        while q:
            x, y, removed = q.popleft()
            if x == m - 1 and y == n - 1:
                return removed

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if grid[nx][ny]:
                        q.append((nx, ny, removed + 1))
                    else:
                        q.appendleft((nx, ny, removed))
        return -1


ans = Solution().minimumObstacles([[0, 1, 1], [1, 1, 0], [1, 1, 0]])
print(ans)

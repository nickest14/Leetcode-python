# 827. Making A Large Island

from collections import deque
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def bfs(total):
            while q:
                r, c = q.popleft()
                for dir in directions:
                    nr = r + dir[0]
                    nc = c + dir[1]

                    if (
                        0 <= nr < m
                        and 0 <= nc < n
                        and grid[nr][nc] == 1
                        and visited[nr][nc] == -1
                    ):
                        q.append((nr, nc))
                        visited[nr][nc] = 1
                        grid[nr][nc] = id
                        total += 1
            island_max[id] = total  # Store the size of this island
            return total

        m: int = len(grid)
        n: int = len(grid[0])
        visited: list[list[int]] = [[-1] * n for _ in range(m)]
        island_max: dict[int, int] = {}
        id: int = 2
        ans: int = 0
        directions: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == -1:
                    total = 1
                    q = deque([(i, j)])
                    visited[i][j] = 1
                    grid[i][j] = id
                    total = bfs(total)
                    ans = max(ans, total)
                    id += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    adjs = set()
                    num = 1

                    for dir in directions:
                        nr = i + dir[0]
                        nc = j + dir[1]

                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 1:
                            adjs.add(grid[nr][nc])

                    for id in adjs:
                        num += island_max[id]

                    ans = max(ans, num)

        return ans


# ans = Solution().largestIsland([[1, 0], [0, 1]])
ans = Solution().largestIsland([[1, 1], [1, 1]])
print(ans)

# 2257. Count Unguarded Cells in the Grid

from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid: list[list[int]] = [[0] * n for _ in range(m)]
        guard: int = 1
        wall: int = 2
        for x, y in guards:
            grid[x][y] = wall
        for x, y in walls:
            grid[x][y] = wall

        directions: list[tuple[int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for gx, gy in guards:
            for dx, dy in directions:
                x, y = gx, gy
                while True:
                    x += dx
                    y += dy
                    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == wall:
                        break
                    grid[x][y] = guard

        return sum(row.count(0) for row in grid)


ans = Solution().countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2,2],[1,4]])
print(ans)

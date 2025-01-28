# 2658. Maximum Number of Fish in a Grid

from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        directions: list[tuple[int, int]] = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ans: int = 0

        def dfs(i: int, j: int):
            if grid[i][j] == 0:
                return 0

            fish: int = grid[i][j]
            grid[i][j] = -1  # Visited

            for dir in directions:
                nr = i + dir[0]
                nc = j + dir[1]
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] > 0:
                        fish += dfs(nr, nc)
            return fish

        for i in range(m):
            for j in range(n):
                if grid[i][j] <= 0:
                    continue
                ans = max(ans, dfs(i, j))
        return ans


ans = Solution().findMaxFish([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]])
print(ans)

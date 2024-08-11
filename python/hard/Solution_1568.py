# 1568. Minimum Number of Days to Disconnect Island

from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        def dfs(visited: list[list[bool]], i: int, j: int):
            m, n = len(grid), len(grid[0])
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 or visited[i][j]:
                return

            visited[i][j] = True
            dfs(visited, i + 1, j)
            dfs(visited, i - 1, j)
            dfs(visited, i, j + 1)
            dfs(visited, i, j - 1)

        def countIslands() -> int:
            visited: list[list[bool]] = [[False] * n for _ in range(m)]
            count = 0

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        count += 1
                        dfs(visited, i, j)  # Explore the island
            return count

        m, n = len(grid), len(grid[0])

        if countIslands() != 1:
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0  # Remove the land cell
                    if countIslands() != 1:
                        return 1
                    grid[i][j] = 1  # Restore the land cell
        return 2


ans = Solution().minDays([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
# ans = Solution().minDays([[1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1]])
print(ans)

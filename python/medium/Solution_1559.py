# 1559. Detect Cycles in 2D Grid

from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        dirs: list[tuple[int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m: int = len(grid)
        n: int = len(grid[0])
        visited: list[bool] = [[False for _ in range(n)] for _ in range(m)]

        def detect(x1: str, y1: str, p1: str, p2: str, prev: str):
            visited[x1][y1] = True
            for dir_1, dir_2 in dirs:
                x = x1 + dir_1
                y = y1 + dir_2
                if (
                    (dir_1 != (-1 * p1) or dir_2 != (-1 * p2))
                    and x >= 0
                    and x < m
                    and y >= 0
                    and y < n
                    and prev == grid[x][y]
                ):
                    if visited[x][y] or detect(x, y, dir_1, dir_2, prev):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if detect(i, j, -1, -1, grid[i][j]):
                        return True
        return False


ans = Solution().containsCycle(
    [
        ["a", "a", "a", "a"],
        ["a", "b", "b", "a"],
        ["a", "b", "b", "a"],
        ["a", "a", "a", "a"],
    ]
)
print(ans)

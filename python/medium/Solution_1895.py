# 1895. Largest Magic Square

from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])

        row: list[list[int]] = [[0] * (n + 1) for _ in range(m)]
        col: list[list[int]] = [[0] * n for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row[i][j + 1] = row[i][j] + grid[i][j]
                col[i + 1][j] = col[i][j] + grid[i][j]

        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target: int = row[i][j + k] - row[i][j]
                    ok: bool = True

                    for r in range(i, i + k):
                        if row[r][j + k] - row[r][j] != target:
                            ok = False

                    for c in range(j, j + k):
                        if col[i + k][c] - col[i][c] != target:
                            ok = False

                    d1 = d2 = 0
                    for x in range(k):
                        d1 += grid[i + x][j + x]
                        d2 += grid[i + x][j + k - 1 - x]

                    if ok and d1 == d2 == target:
                        return k
        return 1


ans = Solution().largestMagicSquare(
    [[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]
)
print(ans)

# 3195. Find the Minimum Area to Cover All Ones I

from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        min_row: int = m
        max_row: int = -1
        min_col: int = n
        max_col: int = -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)

        return (max_row - min_row + 1) * (max_col - min_col + 1)


ans = Solution().minimumArea([[0, 1, 0], [1, 0, 1]])
print(ans)

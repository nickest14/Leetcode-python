# 2684. Maximum Number of Moves in a Grid

from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row: int = len(grid)
        col: int = len(grid[0])
        dp: list[list[int]] = [[0] * col for _ in range(row)]

        for c in range(col - 2, -1, -1):
            for r in range(row):
                if r > 0 and grid[r][c] < grid[r - 1][c + 1]:
                    dp[r][c] = max(dp[r][c], dp[r - 1][c + 1] + 1)
                if grid[r][c] < grid[r][c + 1]:
                    dp[r][c] = max(dp[r][c], dp[r][c + 1] + 1)
                if r < row - 1 and grid[r][c] < grid[r + 1][c + 1]:
                    dp[r][c] = max(dp[r][c], dp[r + 1][c + 1] + 1)

        return max(dp[r][0] for r in range(row))


ans = Solution().maxMoves([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]])
print(ans)

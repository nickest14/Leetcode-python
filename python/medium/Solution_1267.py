# 1267. Count Servers that Communicate

from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows: list[int] = [sum(row) for row in grid]
        cols = [
            sum(grid[row][col] for row in range(len(grid)))
            for col in range(len(grid[0]))
        ]

        ans: int = 0
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    ans += 1

        return ans


ans = Solution().countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
print(ans)

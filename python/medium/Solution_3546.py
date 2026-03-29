# 3546. Equal Sum Grid Partition I

from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total: int = sum(sum(row) for row in grid)

        if total % 2:
            return False

        target: int = total // 2
        s: int = 0

        for i in range(m - 1):
            s += sum(grid[i])
            if s == target:
                return True

        s = 0
        for j in range(n - 1):
            for i in range(m):
                s += grid[i][j]
            if s == target:
                return True

        return False


ans = Solution().canPartitionGrid([[1, 4], [2, 3]])
print(ans)

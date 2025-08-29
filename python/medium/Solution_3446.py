# 3446. Sort Matrix by Diagonals

from typing import List
from heapq import heappush, heappop


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m: int = len(grid[0])
        n: int = len(grid)
        diags: dict[int, list[int]] = {}

        for i in range(n):
            for j in range(m):
                key: int = i - j
                if key not in diags:
                    diags[key] = []
                if key < 0:
                    heappush(diags[key], grid[i][j])
                else:
                    heappush(diags[key], -grid[i][j])

        for i in range(n):
            for j in range(m):
                key = i - j
                if key < 0:
                    grid[i][j] = heappop(diags[key])
                else:
                    grid[i][j] = -heappop(diags[key])
        return grid


ans = Solution().sortMatrix([[1, 7, 3], [9, 8, 2], [4, 5, 6]])

print(ans)

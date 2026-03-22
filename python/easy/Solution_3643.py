# 3643. Flip Square Submatrix Vertically
from typing import List


class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        for i in range(x, x + k // 2):
            mirror: int = x + k - 1 - (i - x)
            for j in range(y, y + k):
                grid[i][j], grid[mirror][j] = grid[mirror][j], grid[i][j]
        return grid


ans = Solution().reverseSubmatrix(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 1, 0, 3
)
print(ans)

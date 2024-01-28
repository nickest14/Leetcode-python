# 2017. Grid Game

from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        ans = float('inf')
        left, right = 0, sum(grid[0])

        for row1, row2 in zip(grid[0], grid[1]):
            right -= row1
            ans = min(ans, max(left, right))
            left += row2
        return ans


ans = Solution().gridGame([[1, 3, 1, 15], [1, 3, 3, 1]])
print(ans)

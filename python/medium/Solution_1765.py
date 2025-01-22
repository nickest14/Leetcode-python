# 1765. Map of Highest Peak

from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows: int = len(isWater)
        cols: int = len(isWater[0])
        height: list[list[int]] = [[float("inf")] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                else:
                    if i > 0:
                        height[i][j] = min(height[i][j], height[i - 1][j] + 1)
                    if j > 0:
                        height[i][j] = min(height[i][j], height[i][j - 1] + 1)

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i < rows - 1:
                    height[i][j] = min(height[i][j], height[i + 1][j] + 1)
                if j < cols - 1:
                    height[i][j] = min(height[i][j], height[i][j + 1] + 1)

        return height


ans = Solution().highestPeak([[0, 1], [0, 0]])
print(ans)

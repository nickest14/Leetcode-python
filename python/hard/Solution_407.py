# 407. Trapping Rain Water II

from typing import List
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m: int = len(heightMap)
        n: int = len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        heap: list[int] = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1
        level: int = 0
        ans: int = 0
        while heap:
            height, x, y = heapq.heappop(heap)
            level = max(level, height)
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n and heightMap[i][j] != -1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))

                    if heightMap[i][j] < level:
                        ans += level - heightMap[i][j]
                    heightMap[i][j] = -1
        return ans


ans = Solution().trapRainWater(
    [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
)
print(ans)

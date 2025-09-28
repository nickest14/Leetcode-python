# 812. Largest Triangle Area

from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n: int = len(points)
        ans: int = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                    ans = max(ans, area)
        return ans


ans = Solution().largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]])
print(ans)

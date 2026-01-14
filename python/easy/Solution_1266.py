# 1266. Minimum Time Visiting All Points

from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time: int = 0
        for i in range(len(points) - 1):
            time += max(
                abs(points[i][0] - points[i + 1][0]),
                abs(points[i][1] - points[i + 1][1]),
            )
        return time


ans = Solution().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]])
print(ans)

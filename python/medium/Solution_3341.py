# 3341. Find Minimum Time to Reach Last Room I

from typing import List
import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        dist: list[list[int]] = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0
        heap: list[tuple[int, int, int]] = [(0, 0, 0)]  # time, row, col

        while heap:
            time, r, c = heapq.heappop(heap)
            if (r, c) == (m - 1, n - 1):
                return time

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    wait_time = max(time, moveTime[nr][nc]) + 1
                    if wait_time < dist[nr][nc]:
                        dist[nr][nc] = wait_time
                        heapq.heappush(heap, (wait_time, nr, nc))
        return -1


# ans = Solution().minTimeToReach([[0, 4], [4, 4]])
# ans = Solution().minTimeToReach([[0,8],[9,10], [1,1]])
ans = Solution().minTimeToReach([[0, 0, 0, 0], [0, 0, 0, 0]])
print(ans)

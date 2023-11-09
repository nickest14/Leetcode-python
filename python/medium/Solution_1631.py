# 1631. Path With Minimum Effort

from typing import List
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        min_heap = [[0, 0, 0]]  # [diff, r, c]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()

        while min_heap:
            diff, r, c = heapq.heappop(min_heap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if (r, c) == (rows - 1, cols - 1):
                return diff

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (new_r < 0 or new_c < 0 or new_r == rows or new_c == cols):
                    continue
                new_diff = max(diff, abs(heights[r][c] - heights[new_r][new_c]))
                heapq.heappush(min_heap, [new_diff, new_r, new_c])


ans = Solution().minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]])
print(ans)

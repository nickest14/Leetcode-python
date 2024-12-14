# 2577. Minimum Time to Visit a Cell In a Grid

from typing import List
import heapq


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        directions: list[tuple[int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m, n = len(grid), len(grid[0])
        heap = [(0, 0, 0)]  # (time, row, col)
        visited = [[False] * n for _ in range(m)]

        while heap:
            time, row, col = heapq.heappop(heap)

            if row == m - 1 and col == n - 1:
                return time

            if visited[row][col]:
                continue
            visited[row][col] = True

            for dr, dc in directions:
                r, c = row + dr, col + dc

                if 0 <= r < m and 0 <= c < n and not visited[r][c]:
                    if grid[r][c] <= time + 1:
                        heapq.heappush(heap, (time + 1, r, c))
                    else:
                        diff = grid[r][c] - time
                        if diff % 2 == 1:
                            heapq.heappush(heap, (grid[r][c], r, c))
                        else:
                            heapq.heappush(heap, (grid[r][c] + 1, r, c))

        return -1


ans = Solution().minimumTime([[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]])
# ans = Solution().minimumTime([[0, 1, 4], [3, 4, 1], [1, 0, 4]])
print(ans)
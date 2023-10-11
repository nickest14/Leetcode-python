# 1162. As Far from Land as Possible

from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    q.append([r, c])
        ans = -1
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q:
            r, c = q.popleft()
            ans = grid[r][c]
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (min(new_r, new_c) >= 0 and max(new_r, new_c) < n and grid[new_r][new_c] == 0):
                    q.append([new_r, new_c])
                    grid[new_r][new_c] = grid[r][c] + 1

        return ans - 1 if ans > 1 else -1


ans = Solution().maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]])
print(ans)

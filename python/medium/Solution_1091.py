# 1091. Shortest Path in Binary Matrix

from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque([(0, 0, 1)])  # r, c , length
        visit = set((0, 0))
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        while q:
            r, c, length = q.popleft()
            if (min(r, c) < 0 or max(r, c) >= n or grid[r][c]):
                continue
            if r == n - 1 and c == n - 1:
                return length
            for dr, dc in direct:
                if (r + dr, c + dc) not in visit:
                    q.append((r + dr, c + dc, length + 1))
                visit.add((r + dr, c + dc))
        return -1


ans = Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]])
print(ans)


# lookup = {sum(d > distanceThreshold for d in row): i for i, row in enumerate(matrix)}

# lookup = {}
# for i, row in enumerate(matrix):
#     count = 0
#     for d in row:
#         if d > distanceThreshold:
#             count += 1
#     lookup[count] = i

# 391. Check if There is a Valid Path in a Grid

from typing import List

from collections import deque


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dirs = {
            1: {0, 1},
            2: {2, 3},
            3: {0, 3},
            4: {1, 3},
            5: {0, 2},
            6: {1, 2},
        }
        moves = [
            (0, -1, 0, 1),
            (0, 1, 1, 0),
            (-1, 0, 2, 3),
            (1, 0, 3, 2),
        ]
        rows: int = len(grid)
        cols: int = len(grid[0])
        visited: list[list[bool]] = [[False] * cols for _ in range(rows)]
        visited[0][0] = True
        queue = deque([(0, 0)])

        while queue:
            row, col = queue.popleft()
            if row == rows - 1 and col == cols - 1:
                return True
            for dr, dc, dx, dy in moves:
                nr = row + dr
                nc = col + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and not visited[nr][nc]
                    and dx in dirs[grid[row][col]]
                    and dy in dirs[grid[nr][nc]]
                ):
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        return False


ans = Solution().hasValidPath([[2,4,3],[6,5,2]])
print(ans)

# 778. Swim in Rising Water

from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n: int = len(grid)
        directions: list[tuple[int, int]] = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(x: int, y: int, t: int, visited: List[List[bool]]):
            if x == n - 1 and y == n - 1:
                return True
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < n
                    and 0 <= ny < n
                    and not visited[nx][ny]
                    and grid[nx][ny] <= t
                ):
                    if dfs(nx, ny, t, visited):
                        return True
            return False

        ans: int = float("inf")
        low, high = 0, n * n - 1
        while low <= high:
            mid: int = (low + high) // 2
            visited: List[List[bool]] = [[False] * n for _ in range(n)]
            if grid[0][0] <= mid and dfs(0, 0, mid, visited):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


ans = Solution().swimInWater([[0, 2], [1, 3]])
print(ans)

# 1905. Count Sub Islands

from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m: int = len(grid1)
        n: int = len(grid1[0])

        def dfs(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
                return

            grid2[i][j] = 0
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        # Remove not exist sub-islands
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)

        ans: int = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    dfs(i, j)
                    ans += 1
        return ans


grid1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
grid2 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
ans = Solution().countSubIslands(grid1, grid2)
print(ans)

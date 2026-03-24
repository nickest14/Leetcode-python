# 2906. Construct Product Matrix

from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod: int = 12345
        m, n = len(grid), len(grid[0])
        ans: list[list[int]] = [[0] * n for _ in range(m)]

        suffix: int = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                ans[i][j] = suffix
                suffix = (suffix * (grid[i][j] % mod)) % mod

        prefix: int = 1
        for i in range(m):
            for j in range(n):
                ans[i][j] = (ans[i][j] * prefix) % mod
                prefix = (prefix * (grid[i][j] % mod)) % mod

        return ans


ans = Solution().constructProductMatrix([[1, 2], [3, 4]])
print(ans)

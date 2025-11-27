# 2435. Paths in Matrix Whose Sum Is Divisible by K

from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod: int = 10**9 + 7
        m: int = len(grid)
        n: int = len(grid[0])

        prev: list[list[int]] = [[0] * k for _ in range(n)]
        cur: list[list[int]] = [[0] * k for _ in range(n)]

        for i in range(m):
            for j in range(n):
                for r in range(k):
                    cur[j][r] = 0

            for j in range(n):
                val = grid[i][j] % k

                if i == 0 and j == 0:
                    cur[0][val] = 1
                    continue

                if i > 0:
                    for r in range(k):
                        if prev[j][r] == 0:
                            continue
                        nr = (r + val) % k
                        cur[j][nr] = (cur[j][nr] + prev[j][r]) % mod

                if j > 0:
                    for r in range(k):
                        if cur[j - 1][r] == 0:
                            continue
                        nr = (r + val) % k
                        cur[j][nr] = (cur[j][nr] + cur[j - 1][r]) % mod

            prev, cur = cur, prev

        return prev[n - 1][0]


ans = Solution().numberOfPaths([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3)
print(ans)

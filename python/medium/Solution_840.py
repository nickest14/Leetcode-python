# 840. Magic Squares In Grid

from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        x, y = len(grid), len(grid[0])

        def is_magic_squares(r, c):
            s = [grid[r + i][c + j] for i in range(3) for j in range(3)]
            if sorted(s) != list(range(1, 10)):
                return False
            return (
                s[0] + s[1] + s[2] == s[3] + s[4] + s[5] == s[6] + s[7] + s[8] == 15
                and s[0] + s[3] + s[6] == s[1] + s[4] + s[7] == s[2] + s[5] + s[8] == 15
                and s[0] + s[4] + s[8] == s[2] + s[4] + s[6] == 15
            )

        ans: int = 0
        for i in range(x - 2):
            for j in range(y - 2):
                if is_magic_squares(i, j):
                    ans += 1
        return ans


ans = Solution().numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]])
print(ans)

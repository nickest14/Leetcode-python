# 1277. Count Square Submatrices with All Ones

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row: int = len(matrix)
        col: int = len(matrix[0])

        dp: list[list[int]] = [[0] * col for _ in range(row)]
        ans: int = 0

        # Initial the first col of dp table
        for i in range(row):
            if matrix[i][0]:
                dp[i][0] = 1
                ans += 1

        # Initial the first row of dp table
        for j in range(1, col):
            if matrix[0][j]:
                dp[0][j] = 1
                ans += 1

        # Fill the dp table for remaining cells
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
                ans += dp[i][j]

        return ans


ans = Solution().countSquares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]])
print(ans)

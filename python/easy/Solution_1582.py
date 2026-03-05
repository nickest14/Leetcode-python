# 1582. Special Positions in a Binary Matrix

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows: int = len(mat)
        cols: int = len(mat[0])
        row_sum: list[int] = [0] * rows
        col_sum: list[int] = [0] * cols
        for i in range(rows):
            for j in range(cols):
                row_sum[i] += mat[i][j]
                col_sum[j] += mat[i][j]

        ans: int = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    ans += 1
        return ans


ans = Solution().numSpecial([[1,0,0],[0,0,1],[1,0,0]])
print(ans)

# 1605. Find Valid Matrix Given Row and Column Sums

from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows: int = len(rowSum)
        cols: int = len(colSum)
        cur_row: int = 0
        cur_col: int = 0
        ans: list[list[int]] = [[0 for _ in range(cols)] for _ in range(rows)]

        while cur_row < rows or cur_col < cols:
            if cur_row >= rows:
                cur_col += 1
                continue
            elif cur_col >= cols:
                cur_row += 1
                continue

            value: int = min(rowSum[cur_row], colSum[cur_col])
            rowSum[cur_row] -= value
            colSum[cur_col] -= value
            ans[cur_row][cur_col] = value

            if rowSum[cur_row] == 0:
                cur_row += 1
            if colSum[cur_col] == 0:
                cur_col += 1

        return ans


ans = Solution().restoreMatrix([5, 7, 10], [8, 6, 8])
# ans = Solution().restoreMatrix([1, 0, 0, 0], [1])
print(ans)

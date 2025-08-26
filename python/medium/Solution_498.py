# 498. Diagonal Traverse

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        ans: list[int] = []
        row: int = 0
        col: int = 0

        for _ in range(m * n):
            ans.append(mat[row][col])

            if (row + col) % 2 == 0:
                if col == n - 1:
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1
            else:
                if row == m - 1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1

        return ans


ans = Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(ans)

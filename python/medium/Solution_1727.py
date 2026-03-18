# 1727. Largest Submatrix With Rearrangements

from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m: int = len(matrix)
        n: int = len(matrix[0])
        ans: int = 0

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        for i in range(m):
            matrix[i].sort(reverse=True)
            for j in range(n):
                ans = max(ans, matrix[i][j] * (j + 1))

        return ans


ans = Solution().largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]])
print(ans)

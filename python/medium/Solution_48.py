# 48. Rotate Image

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        length = len(matrix)
        for i in range(0, length):
            for j in range(i + 1, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # # Another solution:
        # matrix[::] = zip(*matrix[::-1])


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Solution().rotate(matrix)
print(matrix)

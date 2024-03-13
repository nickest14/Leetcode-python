# 304. Range Sum Query 2D - Immutable

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.sum_ = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i, line in enumerate(matrix):
            previous = 0
            for j, num in enumerate(line):
                previous += num
                above = self.sum_[i][j + 1]
                self.sum_[i + 1][j + 1] = previous + above
        print(self.sum_)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum_[row2 + 1][col2 + 1] \
            - self.sum_[row1][col2 + 1] \
            - self.sum_[row2 + 1][col1] \
            + self.sum_[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5],
]

obj = NumMatrix(matrix)
param_1 = obj.sumRegion(2, 1, 4, 3)
param_2 = obj.sumRegion(1, 1, 2, 2)
param_3 = obj.sumRegion(1, 2, 2, 4)
print(param_1)
print(param_2)
print(param_3)

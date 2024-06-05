# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            if target <= matrix[row][cols - 1]:
                for col in range(cols):
                    if target == matrix[row][col]:
                        return True


matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
ans = Solution().searchMatrix(matrix, 16)
print(ans)

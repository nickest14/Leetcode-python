# 54. Spiral Matrix

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # top row
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1

            # right col
            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break

            # bottom row
            for i in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom - 1][i])
            bottom -= 1

            # left col
            for i in range(bottom - 1, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1

        return ans


ans = Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(ans)

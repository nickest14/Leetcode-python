# 1975. Maximum Matrix Sum

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_count: int = 0
        min_value = float("inf")
        sum_abs: int = 0
        for row in matrix:
            for val in row:
                if val < 0:
                    neg_count += 1
                sum_abs += abs(val)
                min_value = min(min_value, abs(val))

        if neg_count % 2 != 0:
            sum_abs -= 2 * min_value

        return sum_abs


ans = Solution().maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]])
print(ans)

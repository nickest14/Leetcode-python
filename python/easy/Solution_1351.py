# 1351. Count Negative Numbers in a Sorted Matrix

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans: int = 0

        for row in grid:
            first_negative = len(row)
            for i, value in enumerate(row):
                if value < 0:
                    first_negative = i
                    break
            ans += len(row) - first_negative
        return ans


ans = Solution().countNegatives(
    [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
)
print(ans)

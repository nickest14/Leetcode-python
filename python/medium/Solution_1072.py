# 1072. Flip Columns For Maximum Number of Equal Rows

from typing import List
from collections import defaultdict


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count: dict[tuple[int], int] = defaultdict(int)
        for row in matrix:
            row_key = tuple(row)
            if row[0]:
                row_key = tuple([0 if r else 1 for r in row])

            count[row_key] += 1

        return max(count.values())


ans = Solution().maxEqualRowsAfterFlips([[0, 0, 0], [0, 0, 1], [1, 1, 0]])
print(ans)

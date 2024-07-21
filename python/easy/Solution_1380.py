# 1380. Lucky Numbers in a Matrix

from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        return list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})


ans = Solution().luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]])
print(ans)

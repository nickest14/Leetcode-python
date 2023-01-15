# 119. Pascal's Triangle II

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for _ in range(rowIndex):
            ans = [x + y for x, y in zip(ans + [0], [0] + ans)]
        return ans


# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
ans = Solution().getRow(4)
print(ans)

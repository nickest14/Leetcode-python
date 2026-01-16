# 2943. Maximize Area of Square Hole in Grid
from typing import List


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        def longest(bars: List[int]) -> int:
            bars.sort()
            best = cur = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    cur += 1
                else:
                    cur = 1
                best = max(best, cur)
            return best + 1

        side: int = min(longest(hBars), longest(vBars))
        return side * side


ans = Solution().maximizeSquareHoleArea(2, 1, [2, 3], [2])
print(ans)

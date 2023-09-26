# 554. Brick Wall

from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count_gap = {}  # {position: gap count}
        for r in wall:
            total = 0
            for b in r[:-1]:
                total += b
                count_gap[total] = 1 + count_gap.get(total, 0)

        return len(wall) - max(count_gap.values(), default=0)


ans = Solution().leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]])
print(ans)

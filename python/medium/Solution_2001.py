# 2001. Number of Pairs of Interchangeable Rectangles

from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}
        ans = 0
        for w, h in rectangles:
            count[w / h] = 1 + count.get(w / h, 0)
        for c in count.values():
            ans += (c * (c - 1)) // 2

        return ans


ans = Solution().interchangeableRectangles([[4, 8], [3, 6], [10, 20], [15, 30]])
print(ans)

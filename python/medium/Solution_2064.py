# 2064. Minimized Maximum of Products Distributed to Any Store

import math
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(x):
            stores = 0
            for q in quantities:
                stores += math.ceil(q / x)
            return stores <= n

        left, right = 1, max(quantities)
        ans = 0
        while left <= right:
            x = (left + right) // 2
            if can_distribute(x):
                ans = x
                right = x - 1
            else:
                left = x + 1

        return ans


# ans = Solution().minimizedMaximum(6, [11, 6])
ans = Solution().minimizedMaximum(7, [15, 10, 10])
print(ans)

# 2558. Take Gifts From the Richest Pile

import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort(reverse=True)

        for _ in range(k):
            gifts[0] = int(math.sqrt(gifts[0]))
            gifts.sort(reverse=True)

        return sum(gifts)


ans = Solution().pickGifts([25, 64, 9, 4, 100], 4)
print(ans)

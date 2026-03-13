# 3296. Minimum Number of Seconds to Make Mountain Height Zero

from typing import List
import math


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def can_finish(time: int) -> bool:
            total = 0
            for w in workerTimes:
                k = int((-1 + math.sqrt(1 + 8 * time / w)) / 2)
                total += k
                if total >= mountainHeight:
                    return True
            return False

        lo, hi = 0, max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while lo < hi:
            mid = (lo + hi) // 2
            if can_finish(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo


ans = Solution().minNumberOfSeconds(4, [2, 1, 1])
print(ans)

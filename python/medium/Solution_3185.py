# 3185. Count Pairs That Form a Complete Day II

from typing import List
from collections import defaultdict


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        remainder_count = defaultdict(int)
        ans = 0

        for hour in hours:
            remainder = hour % 24
            complement = (24 - remainder) % 24
            if complement in remainder_count:
                ans += remainder_count[complement]

            remainder_count[remainder] += 1
        return ans


ans = Solution().countCompleteDayPairs([12, 12, 30, 24, 24])
print(ans)

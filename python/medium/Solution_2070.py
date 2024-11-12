# 2070. Most Beautiful Item for Each Query

from typing import List
from bisect import bisect_right


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])

        price_beauty_pairs: list[list[int]] = []  # Build price_beauty_pairs
        max_beauty: int = 0
        for price, beauty in items:
            max_beauty = max(max_beauty, beauty)
            if not price_beauty_pairs or price_beauty_pairs[-1][1] < max_beauty:
                price_beauty_pairs.append((price, max_beauty))

        ans: list[int] = []
        for q in queries:
            idx = bisect_right(price_beauty_pairs, (q, float('inf'))) - 1
            ans.append(price_beauty_pairs[idx][1] if idx >= 0 else 0)

        return ans


ans = Solution().maximumBeauty([[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6])
print(ans)

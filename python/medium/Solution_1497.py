# 1497. Check If Array Pairs Are Divisible by k

from typing import List
from collections import defaultdict


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) % 2 != 0:
            return False

        pairs: int = 0
        mapping: dict[int, int] = defaultdict(int)
        for val in arr:
            key = k - (val % k)
            if mapping[key] > 0:
                mapping[key] -= 1
                pairs += 1
            else:
                mapping[(val % k) or k] += 1
        return pairs == len(arr) / 2


ans = Solution().canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5)
print(ans)

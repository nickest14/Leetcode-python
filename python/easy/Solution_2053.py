# 2053. Kth Distinct String in an Array

from typing import List
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq: dict[str, int] = Counter(arr)
        count: int = 0
        for s in arr:
            if freq[s] == 1:
                count += 1
                if count == k:
                    return s
        return ''


ans = Solution().kthDistinct(["d", "b", "c", "b", "c", "a"], k = 2)
print(ans)

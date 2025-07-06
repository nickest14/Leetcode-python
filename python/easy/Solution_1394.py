# 1636. Sort Array by Increasing Frequency

from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans: int = -1
        count: dict[int, int] = Counter(arr)
        for num, freq in count.items():
            if num == freq:
                ans = max(ans, num)
        return ans


ans = Solution().findLucky([1, 2, 2, 3, 3, 3])
print(ans)

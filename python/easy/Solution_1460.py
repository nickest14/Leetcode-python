# 1460. Make Two Arrays Equal by Reversing Subarrays

from typing import List
from collections import Counter


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)


ans = Solution().canBeEqual([1, 2, 3, 4], [2, 4, 1, 3])
print(ans)

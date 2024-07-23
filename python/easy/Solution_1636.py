# 1636. Sort Array by Increasing Frequency

from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return sorted(nums, key=lambda val: (count[val], -val))


ans = Solution().frequencySort([2, 3, 1, 3, 2])
print(ans)

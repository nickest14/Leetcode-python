# 3005. Count Elements With Maximum Frequency

from typing import List
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq: dict[int, int] = Counter(nums)
        max_freq: int = max(freq.values())
        return sum(count for num, count in freq.items() if count == max_freq)


ans = Solution().maxFrequencyElements([1,2,2,3,1,4])
print(ans)

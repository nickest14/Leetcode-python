# 3442. Maximum Difference Between Even and Odd Frequency I

from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        freq: Counter = Counter(s)
        max_odd: int = max([val for val in freq.values() if val % 2 == 1])
        min_even: int = min([val for val in freq.values() if val % 2 == 0])
        return max_odd - min_even


ans = Solution().maxDifference("aaaaabbc")
print(ans)

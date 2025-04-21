# 2145. Count the Hidden Sequences

from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        cur: int = 0
        min_val: int = 0
        max_val: int = 0
        for diff in differences:
            cur += diff
            min_val = min(min_val, cur)
            max_val = max(max_val, cur)

        return max(0, (upper - lower) - (max_val - min_val) + 1)


ans = Solution().numberOfArrays([1, -3, 4], 1, 6)
# ans = Solution().numberOfArrays([1], 1, 6)
print(ans)

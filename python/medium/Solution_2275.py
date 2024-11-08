# 2275. Largest Combination With Bitwise AND Greater Than Zero

from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans: int = 0
        for i in range(32):
            count: int = sum(1 for candidate in candidates if candidate & (1 << i))
            ans = max(ans, count)

        return ans


ans = Solution().largestCombination([16, 17, 71, 62, 12, 24, 14])
print(ans)

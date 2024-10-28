# 2501. Longest Square Streak in an Array

from typing import List
from math import isqrt


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        ans: int = -1
        map: dict = {}

        for num in nums:
            sqrt = isqrt(num)
            if sqrt ** 2 == num and sqrt in map:
                map[num] = map[sqrt] + 1
                ans = max(ans, map[num])
            else:
                map[num] = 1

        return ans


ans = Solution().longestSquareStreak([4, 3, 6, 16, 8, 2])
print(ans)

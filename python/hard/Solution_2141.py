# 2141. Maximum Running Time of N Computers

from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total: int = sum(batteries)
        left, right = 0, total // n

        while left < right:
            mid: int = (left + right + 1) // 2
            need: int = mid * n
            have: int = sum(min(battery, mid) for battery in batteries)

            if have >= need:
                left = mid
            else:
                right = mid - 1

        return left


ans = Solution().maxRunTime(2, [3, 3, 3])
print(ans)

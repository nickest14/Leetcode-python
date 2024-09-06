# 2028. Find Missing Observations

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m: int = len(rolls)
        total: int = mean * (m + n)
        miss: int = total - sum(rolls)

        if miss > 6 * n or miss < n:
            return []

        q, r = divmod(miss, n)
        return [q + 1] * r + [q] * (n - r)


ans = Solution().missingRolls([3, 2, 4, 3], 4, 2)
print(ans)

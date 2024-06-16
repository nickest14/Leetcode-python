# 3186. Maximum Total Damage With Spell Casting

from typing import List
from collections import Counter


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        frequency = Counter(power)
        p = [0] + sorted(frequency.keys())
        n = len(p)
        if n == 2:
            return frequency[p[1]] * p[1]

        dp = [0] * n
        dp[1] = frequency[p[1]] * p[1]
        dp[2] = max(frequency[p[2]] * p[2] + (dp[1] if p[2] - p[1] > 2 else 0), dp[1])

        for i in range(3, n):
            damage = frequency[p[i]] * p[i]
            if p[i] - p[i - 1] > 2:
                dp[i] = max(dp[i], dp[i - 1] + damage)
            if p[i] - p[i - 2] > 2:
                dp[i] = max(dp[i], dp[i - 2] + damage)
            dp[i] = max(dp[i], dp[i - 3] + damage, dp[i - 1])

        return dp[n - 1]


ans = Solution().maximumTotalDamage([8, 1, 7, 7, 3, 4, 4, 4, 5])
print(ans)

# 3147. Taking Maximum Energy From the Mystic Dungeon

from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n: int = len(energy)
        dp: list[int] = [0] * n
        ans: int = float("-inf")
        for i in range(n - 1, -1, -1):
            dp[i] = energy[i] + (dp[i + k] if i + k < n else 0)
            ans = max(ans, dp[i])
        return ans


ans = Solution().maximumEnergy([5, 2, -10, -5, 1], 3)
print(ans)

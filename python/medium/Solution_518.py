# 518. Coin Change II

from typing import List


class Solution:
    # Time: O(n*m)
    # Memory: O(n) where n = amount
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            coin_value = coins[i]
            next_dp = [0] * (amount + 1)
            next_dp[0] = 1
            for a in range(1, amount + 1):
                next_dp[a] = dp[a]
                if a - coin_value >= 0:
                    next_dp[a] += next_dp[a - coin_value]
            dp = next_dp
        return dp[amount]


ans = Solution().change(5, [1, 2, 5])
print(ans)

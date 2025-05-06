# 790. Domino and Tromino Tiling


class Solution:
    def numTilings(self, n: int) -> int:
        mod: int = 10**9 + 7
        dp: list[int] = [0] * max(n + 1, 4)
        dp[1], dp[2], dp[3] = 1, 2, 5
        for i in range(4, n + 1):
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % mod

        return dp[n]


ans = Solution().numTilings(5)
print(ans)

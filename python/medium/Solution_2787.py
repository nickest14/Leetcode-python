# 2787. Ways to Express an Integer as Sum of Powers


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod: int = 10**9 + 7
        powers: list[int] = []
        i: int = 1
        while True:
            p: int = pow(i, x)
            if p > n:
                break
            powers.append(p)
            i += 1

        dp: list[int] = [0] * (n + 1)
        dp[0] = 1
        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % mod
        return dp[n]


ans = Solution().numberOfWays(10, 2)
print(ans)

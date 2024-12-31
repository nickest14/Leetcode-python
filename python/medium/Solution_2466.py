# 2466. Count Ways To Build Good Strings


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp: list[int] = [0] * (high+ 1)
        dp[0] = 1
        mod: int = 10 ** 9 + 7
        for i in range(min(zero, one), high+ 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % mod
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % mod
        
        ans: int = 0
        for i in range(low, high + 1):
            ans = (ans + dp[i]) % mod
        return ans


# ans = Solution().countGoodStrings(low=3, high=3, zero=1, one=1)
ans = Solution().countGoodStrings(low=2, high=3, zero=2, one=1)
print(ans)

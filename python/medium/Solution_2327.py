# 2327. Number of People Aware of a Secret


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod: int = 10**9 + 7
        if n == 1:
            return 1

        dp: list[int] = [0] * (n + 1)
        dp[1] = 1
        window: int = 0
        for i in range(2, n + 1):
            _enter: int = i - delay
            _exit: int = i - forget
            if _enter >= 1:
                window = (window + dp[_enter]) % mod
            if _exit >= 1:
                window = (window - dp[_exit] + mod) % mod
            dp[i] = window
            
        start: int = max(1, n - forget + 1)
        ans: int = sum(dp[start : n + 1]) % mod
        return ans


ans = Solution().peopleAwareOfSecret(6, 2, 4)
print(ans)

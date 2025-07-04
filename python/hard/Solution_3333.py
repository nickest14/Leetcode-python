# 3333. Find the Original Typed String II


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod: int = 10**9 + 7
        if not word:
            return 0

        groups: list[int] = []
        count: int = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        total: int = 1
        for num in groups:
            total = (total * num) % mod

        if k <= len(groups):
            return total

        dp: list[int] = [0] * k
        dp[0] = 1

        for num in groups:
            new_dp: list[int] = [0] * k
            sum_val: int = 0
            for s in range(k):
                if s > 0:
                    sum_val = (sum_val + dp[s - 1]) % mod
                if s > num:
                    sum_val = (sum_val - dp[s - num - 1] + mod) % mod
                new_dp[s] = sum_val
            dp = new_dp

        invalid: int = sum(dp[len(groups) : k]) % mod
        return (total - invalid + mod) % mod


# ans = Solution().possibleStringCount("aabbccdd", 7)
# ans = Solution().possibleStringCount("aaabbc", 4)
ans = Solution().possibleStringCount("aaaaaabcd", 3)
print(ans)

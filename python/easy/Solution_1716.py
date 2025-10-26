# 1716. Calculate Money in Leetcode Bank


class Solution:
    def totalMoney(self, n: int) -> int:
        weeks: int = n // 7
        remain: int = n % 7
        full_weeks_sum: int = weeks * 28 + 7 * (weeks * (weeks - 1) // 2)
        rem_sum: int = remain * (1 + weeks) + (remain * (remain - 1) // 2)
        return full_weeks_sum + rem_sum


ans = Solution().totalMoney(10)
print(ans)

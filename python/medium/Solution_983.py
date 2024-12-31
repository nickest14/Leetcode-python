# 983. Minimum Cost For Tickets


from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp: list[int] = [0 for _ in range(days[-1] + 1)]
        days_set = set(days)
        for i in range(days[-1] + 1):
            if i not in days_set:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(0, i - 1)] + costs[0], dp[max(0, i - 7)]+costs[1], dp[max(0, i - 30)]+ costs[2])
        return dp[-1]


ans = Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15])
print(ans)

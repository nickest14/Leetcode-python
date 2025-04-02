# 2140. Solving Questions With Brainpower

from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n: int = len(questions)
        dp: list[int] = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            points = questions[i][0]
            brain_power = questions[i][1]
            next_q: int = i + brain_power + 1
            take: int = points + (dp[next_q] if next_q < n else 0)
            skip: int = dp[i + 1]
            dp[i] = max(take, skip)

        return dp[0]


ans = Solution().mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]])
print(ans)

# 2438. Range Product Queries of Powers

from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod: int = 10**9 + 7
        powers: list[int] = []
        power: int = 1
        while n > 0:
            if n & 1:
                powers.append(power)
            power *= 2
            n >>= 1

        size: int = len(powers)
        dp: list[list[int]] = [[0] * size for _ in range(size)]
        for i in range(size):
            dp[i][i] = powers[i]
            for j in range(i + 1, size):
                dp[i][j] = (dp[i][j - 1] * powers[j]) % mod

        ans: list[int] = []
        for left, right in queries:
            ans.append(dp[left][right])

        return ans


ans = Solution().productQueries(15, [[0, 1], [2, 2], [0, 3]])
print(ans)

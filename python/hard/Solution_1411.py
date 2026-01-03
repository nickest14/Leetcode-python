# 1411. Number of Ways to Paint N × 3 Grid


class Solution:
    def numOfWays(self, n: int) -> int:
        mod: int = 10**9 + 7
        A = B = 6

        for _ in range(2, n + 1):
            A, B = (2 * A + 2 * B) % mod, (2 * A + 3 * B) % mod

        return (A + B) % mod


ans = Solution().numOfWays(1)
print(ans)

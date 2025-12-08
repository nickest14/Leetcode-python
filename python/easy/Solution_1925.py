# 1935. Maximum Number of Words You Can Type

from math import gcd, sqrt


class Solution:
    def countTriples(self, n: int) -> int:
        ans: int = 0
        for u in range(2, int(sqrt(n)) + 1):
            for v in range(1, u):
                if (u - v) & 1 == 0 or gcd(u, v) != 1:
                    continue
                c = u * u + v * v
                if c > n:
                    continue
                ans += 2 * (n // c)
        return ans


ans = Solution().countTriples(5)
print(ans)

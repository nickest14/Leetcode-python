# 2523. Closest Prime Numbers in Range

from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes: list[bool] = [True] * (right + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(right**0.5) + 1):
            if primes[i]:
                for j in range(i * i, right + 1, i):
                    primes[j] = False

        primes_in_range = [i for i in range(left, right + 1) if primes[i]]

        ans: list[int] = [-1, -1]

        if len(primes_in_range) < 2:
            return [-1, -1]
        min_gap: int = float("inf")

        for i in range(1, len(primes_in_range)):
            gap = primes_in_range[i] - primes_in_range[i - 1]
            if gap < min_gap:
                min_gap = gap
                ans = [primes_in_range[i - 1], primes_in_range[i]]

        return ans


ans = Solution().closestPrimes(10, 19)
print(ans)

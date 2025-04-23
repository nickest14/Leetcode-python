# 2338. Count the Number of Ideal Arrays

from collections import defaultdict
from math import comb

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod: int = 10**9 + 7
        ans: int = 0

        sieve = list(range(maxValue + 1))
        for i in range(2, int(maxValue**0.5) + 1):
            if sieve[i] == i:
                for j in range(i * i, maxValue + 1, i):
                    if sieve[j] == j:
                        sieve[j] = i

        def factors(n: int) -> dict[int, int]:
            exp = defaultdict(int)
            while n > 1:
                smallest_prime = sieve[n]
                exp[smallest_prime] += 1
                n //= smallest_prime
            return exp

        ans = 0
        for i in range(1, maxValue + 1):
            ways = 1
            for exp in factors(i).values():
                ways = (ways * comb(n - 1 + exp, exp)) % mod
            ans += ways % mod
        return ans % mod


ans = Solution().idealArrays(2, 5)
print(ans)

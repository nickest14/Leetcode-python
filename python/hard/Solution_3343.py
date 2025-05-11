# 3343. Count Number of Balanced Permutations

from collections import Counter
from functools import cache
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        count = Counter(int(c) for c in num)
        total = sum(int(c) for c in num)
        mod = 10**9 + 7
        n = len(num)

        @cache
        def dfs(i: int, odd: int, even: int, balance: int) -> int:
            if odd == 0 and even == 0 and balance == 0:
                return 1
            if i < 0 or odd < 0 or even < 0 or balance < 0:
                return 0
            ans = 0
            for j in range(0, count[i] + 1):
                
                print(comb(odd, j))
                print(comb(even, count[i] - j))
                print(dfs(i - 1, odd - j, even - count[i] + j, balance - i * j))

                ans += (
                    comb(odd, j)
                    * comb(even, count[i] - j)
                    * dfs(i - 1, odd - j, even - count[i] + j, balance - i * j)
                )
            return ans % mod

        return 0 if total % 2 else dfs(9, n - n // 2, n // 2, total // 2)


ans = Solution().countBalancedPermutations("123")
# ans = Solution().countBalancedPermutations("9944")
print(ans)

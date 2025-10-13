# 3495. Minimum Operations to Make Array Elements Zero

from typing import List
from functools import lru_cache
import math


class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        mod: int = 10**9 + 7

        @lru_cache(None)
        def dfs(remaining: int, odd_needed: int, index: int, carry: int) -> int:
            if (
                remaining < 0
                or odd_needed < 0
                or remaining + carry.bit_count() < odd_needed
            ):
                return 0
            if remaining == 0:
                return 1 if odd_needed == carry.bit_count() else 0
            if index >= len(nums):
                return 0

            ans: int = 0
            for take in range(remaining + 1):
                ways: int = (
                    math.comb(remaining, take) * pow(nums[index], take, mod) % mod
                )
                new_carry: int = carry + take
                ans += ways * dfs(
                    remaining - take,
                    odd_needed - (new_carry % 2),
                    index + 1,
                    new_carry // 2,
                )
                ans %= mod
            return ans

        return dfs(m, k, 0, 0)


ans = Solution().magicalSum(2, 2, [5, 4, 3, 2, 1])
print(ans)

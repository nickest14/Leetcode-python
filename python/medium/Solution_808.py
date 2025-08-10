# 808. Soup Servings

from math import ceil
from functools import cache


class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1

        n: int = ceil(n / 25)

        @cache
        def dfs(a: int, b: int) -> float:
            if a == 0 and b == 0:
                return 0.5
            if a == 0:
                return 1
            if b == 0:
                return 0

            op1: float = dfs(max(0, a - 4), b)
            op2: float = dfs(max(0, a - 3), max(0, b - 1))
            op3: float = dfs(max(0, a - 2), max(0, b - 2))
            op4: float = dfs(max(0, a - 1), max(0, b - 3))
            return sum([op1, op2, op3, op4]) * 0.25

        return dfs(n, n)


ans = Solution().soupServings(50)
print(ans)

# 1931. Painting a Grid With Three Different Colors
from functools import lru_cache


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        @lru_cache(None)
        def generate(i):
            if i == m:
                return [""]
            ans: list[str] = []
            for s in {"r", "b", "g"}:
                for j in generate(i + 1):
                    if not j or s != j[0]:
                        ans.append(s + j)
            
            return ans

        @lru_cache(None)
        def dp(i: int, prev: str) -> int:
            if i == n:
                return 1
            ans: int = 0
            if not prev:
                for p in generate(0):
                    ans += dp(i + 1, p)
            else:
                for p in generate(0):
                    for k in range(len(p)):
                        if p[k] == prev[k]:
                            break
                    else:
                        ans += dp(i + 1, p)
            return ans

        return dp(0, "") % (10**9 + 7)


ans = Solution().colorTheGrid(1, 2)
print(ans)

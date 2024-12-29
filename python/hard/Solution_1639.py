# 1639. Number of Ways to Form a Target String Given a Dictionary

from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m: int = len(words)
        n: int = len(words[0])
        length: int = len(target)
        dic: list[dict] = [defaultdict(int) for i in range(n)]
        for i in range(m):
            for j in range(n):
                c = words[i][j]
                dic[j][c] += 1

        @lru_cache(maxsize=None)
        def dfs(i: int, j: int):
            if j == length:
                return 1
            elif n - i < length - j:
                return 0

            if target[j] not in dic[i]:
                return dfs(i + 1, j)
            return dfs(i + 1, j) + dic[i][target[j]] * dfs(i + 1, j + 1)

        return dfs(0, 0)


ans = Solution().numWays(["acca", "bbbb", "caca"], "aba")
# ans = Solution().numWays(["abba", "baab"], "bab")
print(ans)

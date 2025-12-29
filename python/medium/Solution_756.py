# 756. Pyramid Transition Matrix

from typing import List
from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        rules = defaultdict(set)
        for a, b, c in allowed:
            rules[a + b].add(c)

        bad: set[str] = set()

        def dfs(row: str, idx: int, nxt: str) -> bool:
            if len(row) == 1:
                return True

            if idx == len(row) - 1:
                if nxt in bad:
                    return False
                ok = dfs(nxt, 0, "")
                if not ok:
                    bad.add(nxt)
                return ok

            key: str = row[idx : idx + 2]
            for c in rules[key]:
                if dfs(row, idx + 1, nxt + c):
                    return True
            return False

        return dfs(bottom, 0, "")


ans = Solution().pyramidTransition("BCD", ["BCC", "CDE", "CEA", "FFF"])
# ans = Solution().pyramidTransition("AAAA", ["AAB","AAC","BCD","BBE","DEF"])
print(ans)

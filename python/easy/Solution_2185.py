# 2185. Counting Words With a Given Prefix

from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans: int = 0
        for word in words:
            if word.startswith(pref):
                ans += 1
        return ans


ans = Solution().prefixCount(["pay", "attention", "practice", "attend"], "at")
print(ans)

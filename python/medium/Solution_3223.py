# 3223. Minimum Length of String After Operations

from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        freq: dict[str, int] = Counter(s)
        ans: int = 0
        for _, v in freq.items():
            if v % 2 == 0:
                ans += 2
            else:
                ans += 1
        return ans


ans = Solution().minimumLength("abaacbcbb")
print(ans)

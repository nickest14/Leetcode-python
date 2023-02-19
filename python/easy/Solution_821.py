# 821. Shortest Distance to a Character

from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        length = len(s)
        ans = [0 if char == c else length for char in s]
        for i in range(1, length):
            ans[i] = min(ans[i], ans[i - 1] + 1)
        for i in reversed(range(length - 1)):
            ans[i] = min(ans[i], ans[i + 1] + 1)
        return ans


s = 'loveleetcode'
c = 'e'
ans = Solution().shortestToChar(s, c)
print(ans)

# 2381. Shifting Letters II

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n: int = len(s)
        prefix: list[int] = [0] * (n + 1)
        for start, end, direct in shifts:
            prefix[start] += 2 * direct - 1
            prefix[end + 1] -= 2 * direct - 1

        accumulate: int = 0
        s = list(s)
        for i in range(n):
            accumulate += prefix[i]
            s[i] = chr((ord(s[i]) - ord("a") + accumulate) % 26 + ord("a"))
        return "".join(s)


ans = Solution().shiftingLetters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]])
print(ans)

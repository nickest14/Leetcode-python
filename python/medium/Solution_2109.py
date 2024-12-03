# 2109. Adding Spaces to a String

from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans: list[str] = []
        prev: int = 0
        for space in spaces:
            ans.append(s[prev:space])
            prev = space
        ans.append(s[prev:])

        return ' '.join(ans)


ans = Solution().addSpaces('LeetcodeHelpsMeLearn', [8, 13, 15])
print(ans)

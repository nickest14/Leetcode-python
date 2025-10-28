# 2125. Number of Laser Beams in a Bank

from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans: int = 0
        prev: int = 0

        for row in bank:
            cur: int = row.count("1")
            if cur > 0:
                ans += prev * cur
                prev = cur

        return ans


ans = Solution().numberOfBeams(["011001", "000000", "010100", "001000"])
print(ans)

# 3208. Alternating Groups II

from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors += colors[: k - 1]
        ans: int = 0
        left: int = 0
        for right in range(len(colors)):
            if right > 0 and colors[right] == colors[right - 1]:
                left = right
            if right - left >= k - 1:
                ans += 1
        return ans


ans = Solution().numberOfAlternatingGroups([0, 1, 0, 1, 0], 3)
print(ans)

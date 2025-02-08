# 3160. Find the Number of Distinct Colors Among the Balls

from typing import List
from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans: list[int] = []
        ball_map: dict[int, int] = {}
        color_freq: dict[int, int] = defaultdict(int)

        for ball, color in queries:
            if old_color := ball_map.get(ball, None):
                if color_freq[old_color] > 1:
                    color_freq[old_color] -= 1
                else:
                    del color_freq[old_color]

            ball_map[ball] = color
            color_freq[color] += 1

            ans.append(len(color_freq))

        return ans


ans = Solution().queryResults(4, [[1, 4], [2, 5], [1, 3], [3, 4]])
print(ans)

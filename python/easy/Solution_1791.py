# 1791. Find Center of Star Graph

from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]


ans = Solution().findCenter([[1, 2], [2, 3], [4, 2]])
print(ans)

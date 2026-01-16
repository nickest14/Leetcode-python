# 2975. Maximum Square Area by Removing Fences From a Field

from typing import List


class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        hFences = sorted([1, m] + hFences)
        vFences = sorted([1, n] + vFences)
        
        h_gaps = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_gaps.add(hFences[j] - hFences[i])
        
        max_common = -1
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                gap = vFences[j] - vFences[i]
                if gap in h_gaps:
                    max_common = max(max_common, gap)
        
        if max_common == -1:
            return -1
        return max_common * max_common


ans = Solution().maximizeSquareArea(4, 3, [2, 3], [2])
print(ans)

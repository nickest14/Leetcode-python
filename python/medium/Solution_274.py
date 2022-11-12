# 274. H-Index

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        for i in range(n):
            if citations[i] < i + 1:
                return i
        return n


ans = Solution().hIndex([3, 0, 6, 1, 5])
print(ans)

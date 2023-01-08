# 1337. The K Weakest Rows in a Matrix

from typing import List
import heapq


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        max_heap, n = [], len(mat[0])
        for i, row in enumerate(mat):
            left, right = 0, n
            while left < right:
                mid = left + (right - left) // 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            heapq.heappush(max_heap, (-left, -i))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [-item[1] for item in heapq.nlargest(k, max_heap)]


mat = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1],
]
ans = Solution().kWeakestRows(mat, k=5)
print(ans)

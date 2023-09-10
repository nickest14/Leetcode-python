# 973. K Closest Points to Origin

from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            min_heap.append((dist, x, y))

        heapq.heapify(min_heap)
        ans = []
        for _ in range(k):
            _, x, y = heapq.heappop(min_heap)
            ans.append([x, y])

        return ans


points = [[1, 3], [-2, 2]]
k = 1
ans = Solution().kClosest(points, k)
print(ans)

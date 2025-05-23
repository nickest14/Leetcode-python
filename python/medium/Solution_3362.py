# 3362. Zero Array Transformation III

from typing import List
from heapq import heappush, heappop

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        delta: list[int] = [0] * (len(nums) + 1)
        heap: list[int] = []
        ops: int = 0
        right: int = 0
        for left, num in enumerate(nums):
            ops += delta[left]
            while right < len(queries) and queries[right][0] == left:
                heappush(heap, -queries[right][1])
                right += 1

            while ops < num:
                if not heap or -heap[0] < left:
                    return -1
                delta[1 - heappop(heap)] -= 1
                ops += 1

        return len(heap)            


ans = Solution().maxRemoval([2, 0, 2], [[0, 2], [0, 2], [1, 1]])

print(ans)

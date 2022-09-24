# 1046. Last Stone Weight

from typing import List

import collections
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1 and heap[0] != 0:
            heaviest = heapq.heappop(heap)
            second = heapq.heappop(heap)
            heapq.heappush(heap, heaviest - second)
        return -heap[0]

# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         counter = collections.Counter(stones)
#         biggest, current = 0, max(stones)
#         while current > 0:
#             if counter[current] == 0:
#                 current -= 1
#             elif biggest == 0:
#                 counter[current] %= 2
#                 if counter[current] == 1:
#                     biggest = current
#                 current -= 1
#             else:
#                 counter[current] -= 1
#                 rest = biggest - current
#                 if rest > current:
#                     biggest = rest
#                 else:
#                     counter[rest] += 1
#                     biggest = 0
#         return biggest


ans = Solution().lastStoneWeight([2, 5, 4, 1, 8, 1])
print(ans)

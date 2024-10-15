# 2530. Maximal Score After Applying K Operations

from typing import List
import math
import heapq


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans: int = 0

        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        while k > 0:
            val: int = -heapq.heappop(max_heap)
            ans += val
            heapq.heappush(max_heap, -1 * (math.ceil(val / 3)))
            k -= 1

        return ans


ans = Solution().maxKelements([1, 10, 3, 3, 3], 3)
print(ans)

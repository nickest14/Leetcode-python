# 1985. Find the Kth Largest Integer in the Array

from typing import List
import heapq


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        max_heap = [-int(n) for n in nums]
        heapq.heapify(max_heap)
        while k > 1:
            heapq.heappop(max_heap)
            k -= 1
        return str(-max_heap[0])


ans = Solution().kthLargestNumber(["3", "6", "7", "10"], 4)
print(ans)

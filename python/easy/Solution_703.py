# 703. Kth Largest Element in a Stream

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap_list = nums
        heapq.heapify(nums)
        while len(self.heap_list) > k:
            heapq.heappop(self.heap_list)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap_list, val)
        if len(self.heap_list) > self.k:
            heapq.heappop(self.heap_list)
        return self.heap_list[0]


# Your KthLargest object will be instantiated and called as such:
k = 3
nums = [1, 3, 2, 5, 8, 10]
obj = KthLargest(k, nums)
param_1 = obj.add(11)
print(param_1)

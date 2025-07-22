# 2163. Minimum Difference in Sums After Removal of Elements

from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n3: int = len(nums)
        n: int = n3 // 3

        left_min: list[int] = [0] * n3
        right_min: list[int] = [0] * n3

        max_heap: list[int] = []
        left_sum: int = 0
        for i in range(n3):
            heapq.heappush(max_heap, -nums[i])
            left_sum += nums[i]
            if len(max_heap) > n:
                left_sum += heapq.heappop(max_heap)
            if i >= n - 1:
                left_min[i] = left_sum

        min_heap: list[int] = []
        right_sum: int = 0
        for i in range(n3 - 1, -1, -1):
            heapq.heappush(min_heap, nums[i])
            right_sum += nums[i]
            if len(min_heap) > n:
                right_sum -= heapq.heappop(min_heap)
            if i <= n3 - n:
                right_min[i] = right_sum

        ans: int = float('inf')
        for i in range(n - 1, n3 - n):
            ans = min(ans, left_min[i] - right_min[i + 1])

        return ans



ans = Solution().minimumDifference([7, 9, 5, 8, 1, 3])
print(ans)

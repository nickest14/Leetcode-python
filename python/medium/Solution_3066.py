# 3066. Minimum Operations to Exceed Threshold Value II

from typing import List
import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans: int = 0
        while len(nums) > 1:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            if x >= k:
                return ans
            heapq.heappush(nums, x*2 + y)
            ans += 1

        if heapq.heappop(nums) >= k:
            return ans
        else:
            return -1


# ans = Solution().minOperations([2, 11, 10, 1, 3], 10)
ans = Solution().minOperations([1,1,2,4,9], 20)
print(ans)

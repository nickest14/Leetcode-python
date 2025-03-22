# 2560. House Robber IV

from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_steal_k_houses(capability: int) -> bool:
            count: int = 0
            i: int = 0
            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= k

        left, right = min(nums), max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if can_steal_k_houses(mid):
                right = mid
            else:
                left = mid + 1

        return left


ans = Solution().minCapability([2, 3, 5, 9], 2)
# ans = Solution().minCapability([2, 2, 10, 10, 10, 10, 8], 3)
print(ans)

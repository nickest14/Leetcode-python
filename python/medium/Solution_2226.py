# 2226. Maximum Candies Allocated to K Children

from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        def canDistribute(val: int) -> bool:
            return sum(c // val for c in candies) >= k

        ans: int = 0
        left, right = 1, max(candies)
        while left <= right:
            mid = (left + right) // 2
            if canDistribute(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


ans = Solution().maximumCandies([5, 8, 6], 3)
# ans = Solution().maximumCandies([1], 1)
print(ans)

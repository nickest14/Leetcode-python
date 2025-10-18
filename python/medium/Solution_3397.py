# 3397. Maximum Number of Distinct Elements After Operations

from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans: int = 0
        prev: int = -(1 << 31)
        for num in nums:
            low: int = num - k
            high: int = num + k
            cur: int = prev + 1
            if cur < low:
                cur = low
            if cur <= high:
                ans += 1
                prev = cur
        return ans


ans = Solution().maxDistinctElements([1, 2, 2, 3, 3, 4], 2)
# ans = Solution().maxDistinctElements([5, 5, 5, 5], 2)

print(ans)

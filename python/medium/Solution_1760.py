# 1760. Minimum Limit of Balls in a Bag

from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low, high = 1, max(nums)
        while low < high:
            mid: int = (low + high) // 2
            ops: int = 0
            for num in nums:
                ops += (num - 1) // mid
            if ops <= maxOperations:
                high = mid
            else:
                low = mid + 1

        return high


ans = Solution().minimumSize([9, 6], 2)
# ans = Solution().minimumSize([9, 5], 2)
print(ans)

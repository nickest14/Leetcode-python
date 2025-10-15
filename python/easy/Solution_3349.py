# 3349. Adjacent Increasing Subarrays Detection I

from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        inc: int = 1
        prev_inc: int = 0
        max_len: int = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
            else:
                prev_inc = inc
                inc = 1
            max_len = max(max_len, max(inc >> 1, min(prev_inc, inc)))
            if max_len >= k:
                return True
        return False


ans = Solution().hasIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1], 3)
print(ans)

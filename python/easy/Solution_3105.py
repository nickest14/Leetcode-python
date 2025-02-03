# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n: int = len(nums)
        if n == 1:
            return 1
        inc: int = 1
        dec: int = 1
        ans: int = 0

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            ans = max(ans, inc, dec)
        return ans


ans = Solution().longestMonotonicSubarray([1, 4, 3, 3, 2])
print(ans)

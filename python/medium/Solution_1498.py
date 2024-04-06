# 1498. Number of Subsequences That Satisfy the Given Sum Condition

from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, mod = 0, (10**9 + 7)
        left, right = 0, len(nums) - 1

        while left <= right:
            if (nums[left] + nums[right]) > target:
                right -= 1
            else:
                ans += 2 ** (right - left)
                left += 1
        return ans % mod


ans = Solution().numSubseq([3, 5, 6, 7], 999)
print(ans)

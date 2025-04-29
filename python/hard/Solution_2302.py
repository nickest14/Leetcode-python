# 2302. Count Subarrays With Score Less Than K

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans: int = 0
        left, partial_sum = 0, 0
        for right in range(len(nums)):
            partial_sum += nums[right]
            while partial_sum * (right - left + 1) >= k:
                partial_sum -= nums[left]
                left += 1
            ans += right - left + 1

        return ans


ans = Solution().countSubarrays([2, 1, 4, 3, 5], 10)
print(ans)

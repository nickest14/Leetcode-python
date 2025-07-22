# 1695. Maximum Erasure Value

from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen: set[int] = set()
        left: int = 0
        current_sum: int = 0
        ans: int = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                current_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
            current_sum += nums[right]
            seen.add(nums[right])
            ans = max(ans, current_sum)

        return ans


ans = Solution().maximumUniqueSubarray([4, 2, 4, 5, 6])
print(ans)

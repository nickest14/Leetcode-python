# 1838. Frequency of the Most Frequent Element

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, 0
        ans, total = 0, 0
        while r < len(nums):
            total += nums[r]
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            ans = max(ans, r - l + 1)
            r += 1

        return ans


# ans = Solution().maxFrequency([1, 2, 4], 5)
ans = Solution().maxFrequency([1, 4, 8, 13], 5)
print(ans)

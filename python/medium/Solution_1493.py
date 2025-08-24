# 1493. Longest Subarray of 1's After Deleting One Element

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans: int = 0
        left: int = 0
        zeros: int = 0

        for right, num in enumerate(nums):
            if num == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            ans = max(ans, right - left)
        return ans


ans = Solution().longestSubarray([1, 1, 0, 1])
print(ans)

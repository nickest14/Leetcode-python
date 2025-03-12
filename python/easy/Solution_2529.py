# 2529. Maximum Count of Positive Integer and Negative Integer

from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n: int = len(nums)
        left, right = 0, n - 1
        # Find the index of the first positive number
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1
        positive_count: int = n - left

        left, right = 0, n - 1
        # Find the last negative number using binary search
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1
        negative_count = right + 1

        return max(positive_count, negative_count)


ans = Solution().maximumCount([-2, -1, -1, 1, 2, 3])
print(ans)

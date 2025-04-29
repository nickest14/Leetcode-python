# 2962. Count Subarrays Where Max Element Appears at Least K Times

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans: int = 0
        max_value: int = max(nums)
        max_count: int = 0
        n: int = len(nums)
        left: int = 0

        for right in range(n):
            if nums[right] == max_value:
                max_count += 1
            while max_count >= k:
                ans += n - right
                if nums[left] == max_value:
                    max_count -= 1
                left += 1
        return ans


ans = Solution().countSubarrays([1, 3, 2, 3, 3], 2)
print(ans)

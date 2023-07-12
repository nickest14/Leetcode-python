# 153. Find Minimum in Rotated Sorted Array

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break
            m = (l + r) // 2
            ans = min(ans, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return ans


ans = Solution().findMin([3, 4, 5, 1, 2])
print(ans)

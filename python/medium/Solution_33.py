# 33. Search in Rotated Sorted Array

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


# ans = Solution().search([4, 5, 6, 7, 0, 1, 2], 2)
# ans = Solution().search([3, 1], 1)
ans = Solution().search([5, 1, 2, 3, 4], 1)

print(ans)

# 33. Search in Rotated Sorted Array


class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            if target == nums[left]:
                return left
            if target == nums[right]:
                return right
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# ans = Solution().search([4, 5, 6, 7, 0, 1, 2], 2)
# ans = Solution().search([3, 1], 1)
ans = Solution().search([5, 1, 2, 3, 4], 1)

print(ans)

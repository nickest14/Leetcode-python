# 81. Search in Rotated Sorted Array II
class Solution:
    def search(self, nums, target):
        if nums is None:
            return False
        left = 0
        right = len(nums) - 1
        if left == right:
            return nums[left] == target

        while left < right:
            mid = int((left + right) / 2)
            if nums[left] == target or nums[right] == target or nums[mid] == target:
                return True
            if nums[left] < nums[right]:
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[left] == nums[right]:
                    right = right - 1
                elif nums[left] == nums[mid]:
                    left = mid + 1
                elif nums[right] == nums[mid]:
                    right = mid - 1
                elif nums[mid] < target < nums[right]:
                    left = mid + 1
                elif nums[left] < target < nums[mid]:
                    right = mid - 1
                elif nums[left] < nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


ans = Solution().search([3, 5, 6, 0, 0, 1, 2], 4)
print(ans)
ans = Solution().search([1, 1, 3, 1], 3)
print(ans)
ans = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
print(ans)
ans = Solution().search([3, 1, 2, 2, 2], 1)
print(ans)
ans = Solution().search([4, 5, 6, 7, 0, 1, 2], 5)
print(ans)
ans = Solution().search([2, 2, 2, 0, 0, 1], 0)
print(ans)
ans = Solution().search([1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,5,5,5,5,6,6,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,10,10,10,-10,-10,-10,-9,-9,-9,-9,-9,-8,-8,-8,-8,-8,-8,-8,-7,-7,-7,-7,-7,-6,-6,-6,-6,-5,-5,-4,-4,-3,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,-1,0,0,0]
, 8)
print(ans)

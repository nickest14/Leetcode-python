# 35. Search Insert Position


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = low + ((high - low) // 2)
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low


ans = Solution().searchInsert([1, 3, 5, 6], 5)
print(ans)

ans2 = Solution().searchInsert([1, 3, 5, 6], 7)
print(ans2)

ans3 = Solution().searchInsert([1, 3, 5, 6], -1)
print(ans3)

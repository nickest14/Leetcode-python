# 35. Search Insert Position


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return i+1


ans = Solution().searchInsert([1, 3, 5, 6], 5)
print(ans)

ans2 = Solution().searchInsert([1, 3, 5, 6], 7)
print(ans2)

ans3 = Solution().searchInsert([1, 3, 5, 6], -1)
print(ans3)

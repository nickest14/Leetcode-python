# 26. Remove Duplicates from Sorted Array

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 1
        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx - 1]:
                nums[ans] = nums[idx]
                ans += 1
        return ans


ans = Solution().removeDuplicates([2, 7, 7, 7, 7, 11, 15])
print(ans)

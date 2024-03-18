# 665. Non-decreasing Array

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True

        changed = False
        for i, num in enumerate(nums):
            if i == len(nums) - 1 or num <= nums[i + 1]:
                continue
            if changed:
                return False
            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
            changed = True
        return True


ans = Solution().checkPossibility([4, 2, 3])
print(ans)

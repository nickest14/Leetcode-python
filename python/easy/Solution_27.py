# 27. Remove Element

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, last = 0, len(nums)
        while i < last:
            if nums[i] == val:
                last -= 1
                nums[i] = nums[last]
            else:
                i += 1
        return last


ans = Solution().removeElement([3, 3, 2, 1, 2, 3, 6], 3)
print(ans)

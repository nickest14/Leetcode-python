# 1608. Special Array With X Elements Greater Than or Equal X

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        length = len(nums)
        while i < length and nums[i] >= i:
            i += 1
        if nums[i - 1] < i:
            return -1
        return i


ans = Solution().specialArray([0, 4, 3, 0, 4])
print(ans)

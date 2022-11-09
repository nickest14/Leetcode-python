# 1752. Check if Array Is Sorted and Rotated

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i - 1] > nums[i] for i in range(len(nums))) <= 1


ans = Solution().check([3, 4, 5, 1, 2])
print(ans)

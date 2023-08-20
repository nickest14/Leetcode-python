# 55. Jump Game

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        max_index = 0
        for i in range(0, len(nums) - 1):
            if i > max_index:
                # can not reach this index
                return False
            max_index = max(i + nums[i], max_index)
            if max_index >= target:
                return True
        return max_index >= target


ans = Solution().canJump([2, 3, 1, 1, 4])
# ans = Solution().canJump([3, 2, 1, 0, 4])
print(ans)

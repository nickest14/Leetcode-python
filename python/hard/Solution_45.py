# 45. Jump Game II

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0
        ans = 0
        while right < len(nums) - 1:
            max_jump = 0
            for i in range(left, right + 1):
                max_jump = max(max_jump, nums[i] + i)
            left = right + 1
            right = max_jump
            ans += 1
        return ans


nums = [2, 3, 1, 1, 4]
ans = Solution().jump(nums)
print(ans)

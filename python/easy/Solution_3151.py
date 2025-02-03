# 3151. Special Array I

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True


ans = Solution().isArraySpecial([1])
# ans = Solution().isArraySpecial([4, 3, 1, 6])
print(ans)

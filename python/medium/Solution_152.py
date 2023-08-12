# 152. Maximum Product Subarray

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        cur_min, cur_max = 1, 1
        for num in nums:
            temp = cur_max * num
            cur_max = max(num * cur_max, num * cur_min, num)
            cur_min = min(temp, num * cur_min, num)
            ans = max(ans, cur_max)

        return ans


ans = Solution().maxProduct([2, 3, -2, 4])
# ans = Solution().maxProduct([-10, 2, 3, 4])
# ans = Solution().maxProduct([5, 0, 3, 4])
print(ans)

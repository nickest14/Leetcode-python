# 2874. Maximum Value of an Ordered Triplet II

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n: int = len(nums)
        if n < 3:
            return 0
        ans: int = 0
        max_value: int = nums[0]
        max_diff: int = 0
        for i in range(1, n):
            ans = max(ans, max_diff * nums[i])
            max_diff = max(max_diff, max_value - nums[i])
            max_value = max(max_value, nums[i])

        return ans


ans = Solution().maximumTripletValue([12, 6, 1, 2, 7])
print(ans)

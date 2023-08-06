# 198. House Robber

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max, cur_max = 0, 0
        for n in nums:
            temp = max(n + prev_max, cur_max)
            prev_max = cur_max
            cur_max = temp
        return cur_max


ans = Solution().rob([1, 2, 3, 1])
print(ans)

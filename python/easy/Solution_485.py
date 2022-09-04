# 485. Max Consecutive Ones

import itertools
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        groups = itertools.groupby(nums)
        return max(sum(list(g[1]))for g in groups)


# Another Solution
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         count, ans = 0, 0
#         for num in nums:
#             if num > 0:
#                 count += 1
#             else:
#                 ans = max(ans, count)
#                 count = 0
#         return max(ans, count)


nums = [1, 1, 0, 1, 1, 1, 0, 1, 1]
# nums = [0]
ans = Solution().findMaxConsecutiveOnes(nums)
print(ans)

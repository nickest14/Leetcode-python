# 3011. Find if Array Can Be Sorted

from itertools import groupby, chain
from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        grp = groupby(nums, key=lambda x: x.bit_count())
        return list(chain(*[sorted(g) for _, g in grp])) == sorted(nums)


ans = Solution().canSortArray([8, 4, 2, 30, 15])
print(ans)

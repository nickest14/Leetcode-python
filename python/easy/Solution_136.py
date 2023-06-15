# 136. Single Number

from typing import List

import functools
import operator


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return functools.reduce(operator.xor, nums)


ans = Solution().singleNumber([4, 1, 2, 1, 2])
print(ans)

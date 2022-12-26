# 303. Range Sum Query - Immutable

from typing import List
import itertools


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = list(itertools.accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(0, 2)
print(param_1)


param_2 = obj.sumRange(2, 5)
print(param_2)

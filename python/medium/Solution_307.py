# 307. Range Sum Query - Mutable

from typing import List
import copy


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = [0] + nums
        self.BIT = self.nums[:]
        for i in range(1, len(self.BIT)):
            if (j := i + (i & -i)) < len(self.BIT):
                self.BIT[j] += self.BIT[i]

    def update(self, index: int, val: int) -> None:
        index += 1
        delta = val - self.nums[index]
        self.nums[index] = val
        while index < len(self.BIT):
            self.BIT[index] += delta
            index += (index & -index)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right) - self.prefixSum(left - 1)

    def prefixSum(self, index: int) -> int:
        index += 1
        total = 0
        while index > 0:
            total += self.BIT[index]
            index -= (index & -index)
        return total


#  Not pass
# class NumArray:
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.sum_list = copy.deepcopy(nums)
#         self.end = len(nums)-1
#         self.prefixSum()

#     def update(self, index: int, val: int):
#         self.nums[index] = val
#         self.prefixSum(index)

#     def sumRange(self, left: int, right: int):
#         if left == 0:
#             return self.sum_list[right]
#         else:
#             return self.sum_list[right] - self.sum_list[left-1]

#     def prefixSum(self, start: int = 0):
#         if start == 0:
#             temp = 0
#         else:
#             temp = self.sum_list[start-1]
#         count = self.end - start + 1
#         for i in range(count):
#             temp += self.nums[start+i]
#             self.sum_list[start+i] = temp


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
obj = NumArray(nums)
test1 = obj.sumRange(2, 6)
obj.update(1, -50)
test2 = obj.sumRange(0, 3)

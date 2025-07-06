# 1865. Finding Pairs With a Certain Sum

from typing import List
from collections import Counter


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.dic1: dict[int, int] = Counter(nums1)
        self.dic2: dict[int, int] = Counter(nums2)
        self.arr2 = [num for num in nums2]

    def add(self, index: int, val: int) -> None:
        old_val = self.arr2[index]
        self.arr2[index] += val
        self.dic2[old_val] -= 1
        self.dic2[self.arr2[index]] += 1

    def count(self, tot: int) -> int:
        result: int = 0
        for i in self.dic1:
            result += self.dic2[tot - i] * (self.dic1[i])
        return result


test_case = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
print(test_case.count(7))
test_case.add(3, 2)
print(test_case.count(8))
print(test_case.count(4))
test_case.add(0, 1)
test_case.add(1, 1)
print(test_case.count(7))

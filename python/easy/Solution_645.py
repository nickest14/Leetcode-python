# 645. Set Mismatch

from typing import List
import itertools


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mixed, a, b = 0, 0, 0
        for num in itertools.chain(nums, range(1, len(nums) + 1)):
            mixed ^= num
        lsb = mixed & -mixed
        for num in itertools.chain(nums, range(1, len(nums) + 1)):
            if num & lsb == 0:
                a ^= num
            else:
                b ^= num
        return [a, b] if nums.count(a) > 1 else [b, a]


ans = Solution().findErrorNums([1, 2, 2, 4])
print(ans)

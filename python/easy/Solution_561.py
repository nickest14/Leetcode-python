# 561. Array Partition

from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


# import collections
# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         counter = collections.Counter(nums)
#         s, rest = 0, 0
#         for i in range(-10000, 10001):
#             if counter[i] > 0:
#                 if rest > 0:
#                     counter[i] -= 1
#                 half, rest = divmod(counter[i], 2)
#                 s += (half + rest) * i
#         return s


ans = Solution().arrayPairSum([1, 4, 3, 2])
# ans = Solution().arrayPairSum([1, 9, 4, 7, 1, 7])
print(ans)

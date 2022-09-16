# 350. Intersection of Two Arrays II

import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        return sum([[k] * v for k, v in (counter1 & counter2).items()], [])


# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         def gen(N1, N2):
#             try:
#                 n1, n2 = next(N1), next(N2)
#                 while True:
#                     if n1 > n2:
#                         n2 = next(N2)
#                     elif n2 > n1:
#                         n1 = next(N1)
#                     else:
#                         yield n1
#                         n1, n2 = next(N1), next(N2)
#             except StopIteration:
#                 pass

#         return list(gen(*map(iter, map(sorted, (nums1, nums2)))))

nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums2 = [1, 2, 8, 7, 6]
ans = Solution().intersect(nums1, nums2)
print(ans)

for k, v in (counter1 & counter2).items()

# 2215. Find the Difference of Two Arrays

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        li1 = [num for num in nums1_set if num not in nums2_set]
        li2 = [num for num in nums2_set if num not in nums1_set]

        return [li1, li2]


ans = Solution().findDifference([1, 2, 3], [2, 4, 6])
print(ans)

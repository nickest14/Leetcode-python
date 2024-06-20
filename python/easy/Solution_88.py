# 88. Merge Sorted Array

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# Solution().merge([7, 8, 9, 0, 0, 0], 3, [2, 5, 6], 3)

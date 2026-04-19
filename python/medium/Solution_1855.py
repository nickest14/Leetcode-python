# 1855. Maximum Distance Between a Pair of Values

from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i: int = 0
        j: int = 1

        while i < len(nums1) and j < len(nums2):
            i += nums1[i] > nums2[j]
            j += 1

        return j - i - 1


ans = Solution().maxDistance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5])
print(ans)

# 2425. Bitwise XOR of All Pairings

from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans: int = 0
        if len(nums1) % 2 == 1:
            for num in nums2:
                ans ^= num
        if len(nums2) % 2 == 1:
            for num in nums1:
                ans ^= num
        return ans


ans = Solution().xorAllNums([2, 1, 3], [10, 2, 5, 0])
print(ans)

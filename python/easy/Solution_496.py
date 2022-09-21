# 496. Next Greater Element I

import itertools
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) \
            -> List[int]:
        greater, stack = {}, []
        for num in nums2:
            while stack and stack[-1] < num:
                greater[stack.pop()] = num
            stack.append(num)
        return [greater.get(num, -1) for num in nums1]


nums1 = [999, 5, 2, 1]
nums2 = [1, 5, 4, 3, 2, 999, 6]
ans = Solution().nextGreaterElement(nums1, nums2)
print(ans)

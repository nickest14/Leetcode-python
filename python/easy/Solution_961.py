# 961. N-Repeated Element in Size 2N Array

from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)
        return -1


ans = Solution().repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4])
print(ans)

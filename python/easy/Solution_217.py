# 217. Contains Duplicate

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


ans = Solution().containsDuplicate([1, 2, 3, 4, 1])
print(ans)

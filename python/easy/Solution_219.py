# 219. Contains Duplicate II

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for ind, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if ind >= k:
                window.remove(nums[ind - k])
        return False


ans = Solution().containsNearbyDuplicate([1, 2, 3, 1], 3)
print(ans)

# 330. Patching Array

from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count = 0
        i = 0  # Iterate over range nums array
        j = 0  # Iterate over range n
        while j < n:
            if i < len(nums) and nums[i] <= j + 1:
                j += nums[i]
                i += 1
            else:
                j += j + 1
                count += 1
        return count


ans = Solution().minPatches([4, 5], 20)
print(ans)

# 2799. Count Complete Subarrays in an Array

from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans: int = 0
        n: int = len(nums)
        distinct: int = len(set(nums))
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                if len(seen) == distinct:
                    ans += n - j
                    break
        return ans


ans = Solution().countCompleteSubarrays([1, 3, 1, 2, 2])
print(ans)

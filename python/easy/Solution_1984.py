# 1984. Minimum Difference Between Highest And Lowest of K Scores

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, k - 1
        ans: int = float("inf")
        length: int = len(nums)
        while r < length:
            ans = min(ans, nums[r] - nums[l])
            l, r = l + 1, r + 1
        return ans


ans = Solution().minimumDifference([90], 1)
# ans = Solution().minimumDifference([9, 4, 1, 7], 2)
print(ans)

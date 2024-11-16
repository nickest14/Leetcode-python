# 3254. Find the Power of K-Size Subarrays I

from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        n: int = len(nums)
        ans: list[int] = []
        left: int = 0
        right: int = 1
        while right < n:
            is_consecutive: bool = nums[right] - nums[right - 1] == 1
            if not is_consecutive:
                while left < right and left + k - 1 < n:
                    ans.append(-1)
                    left += 1
                left = right
            elif right - left == k - 1:
                ans.append(nums[right])
                left += 1
            right += 1

        return ans


ans = Solution().resultsArray([1, 2, 3, 4, 3, 2, 5], 3)
# ans = Solution().resultsArray([4, 1, 2, 3, 4, 3, 4], 4)
print(ans)

# 3379. Transformed Array

from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        ans: list[int] = [0] * len(nums)

        for i, num in enumerate(nums):
            if num > 0:
                ans[i] = nums[(i + num) % n]
            elif num < 0:
                ans[i] = nums[(i - -num) % n]
            else:
                ans[i] = num
        
        return ans


ans = Solution().constructTransformedArray([3, -2, 1, 1])
print(ans)

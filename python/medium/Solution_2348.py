# 2348. Number of Zero-Filled Subarrays

from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans: int = 0
        zeros: int = 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif zeros > 0:
                ans += (zeros * (zeros + 1)) // 2
                zeros = 0

        ans += (zeros * (zeros + 1)) // 2
        return ans


ans = Solution().zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4])
# ans = Solution().zeroFilledSubarray([0, 0, 0, 2, 0, 0])
print(ans)

# 2598. Smallest Missing Non-negative Integer After Operations

from typing import List
                

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainder_count: list[int] = [0] * value

        for num in nums:
            rem: int = num % value
            remainder_count[rem] += 1

        ans: int = 0
        while remainder_count[ans % value] > 0:
            remainder_count[ans % value] -= 1
            ans += 1

        return ans


ans = Solution().findSmallestInteger([1, -10, 7, 13, 6, 8], 5)
print(ans)

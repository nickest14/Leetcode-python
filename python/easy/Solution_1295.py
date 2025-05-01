# 1295. Find Numbers with Even Number of Digits

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans: int = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                ans += 1
        return ans


ans = Solution().findNumbers([12, 345, 2, 6, 7896])
print(ans)

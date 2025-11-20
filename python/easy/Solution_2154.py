# 2022. Convert 1D Array Into 2D Array

from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        bits: int = 0
        for num in nums:
            if num % original != 0:
                continue
            n: int = num // original
            if n & (n - 1) == 0:
                bits |= n
        digit: int = bits + 1
        return original * (digit & -digit)


ans = Solution().findFinalValue([5,3,6,1,12], 3)
print(ans)

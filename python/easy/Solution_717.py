# 717. 1-bit and 2-bit Characters

from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n: int = len(bits)
        i: int = 0
        while i < n - 1:
            i += bits[i] + 1
        return i == n - 1


ans = Solution().isOneBitCharacter([1, 0, 0])
print(ans)

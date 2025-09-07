# 1304. Find N Unique Integers Sum up to Zero

from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [n * (1 - n) // 2] + list(range(1, n))


ans = Solution().sumZero(5)
print(ans)

# 1317. Convert Integer to the Sum of Two No-Zero Integers

from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i, j, base = 0, 0, 1
        while n > 0:
            n, d = divmod(n, 10)
            if d in (0, 1) and n > 0:
                i += base * (d + 1)
                j += base * 9
                n -= 1
            else:
                i += base * (d - 1)
                j += base
            base *= 10
        return [i, j]


ans = Solution().getNoZeroIntegers(100)
print(ans)

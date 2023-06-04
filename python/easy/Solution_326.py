# 326. Power of Three

import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if (math.log10(n) / math.log10(3)).is_integer():
            return True
        return False


ans = Solution().isPowerOfThree(81)
print(ans)

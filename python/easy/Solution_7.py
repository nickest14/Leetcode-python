# 7. Reverse Integer

import math


class Solution:
    def reverse(self, x: int) -> int:
        min, max = -2**31, 2**31 - 1
        ans = 0

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            if ans > max // 10 or (ans == max // 10 and digit > max % 10):
                return 0
            if ans < min // 10 or (ans == min // 10 and digit < min % 10):
                return 0

            ans = digit + (ans * 10)
        return ans


ans = Solution().reverse(-123)
print(ans)

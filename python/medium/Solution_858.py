# 858. Mirror Reflection

import math


class Solution:
    """
    p is odd, q is odd => receptor 1
    p is odd, q is even => receptor 0
    p is even, q is odd => receptor 2
    """
    def mirrorReflection(self, p: int, q: int) -> int:
        g = math.gcd(p, q)
        p, q = p // g, q // g
        if p % 2 == 0:
            return 2
        return q % 2


ans = Solution().mirrorReflection(3, 1)
print(ans)

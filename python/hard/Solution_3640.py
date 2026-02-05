# 3640. Trionic Array II

from typing import List
import math


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n: int = len(nums)
        a = b = c = ans = -math.inf

        for i in range(1, n):
            x0, x1 = nums[i - 1], nums[i]

            na = nb = nc = -math.inf
            if x0 < x1:
                # phase 1: start new a or extend current inc a
                na = max(x0 + x1, a + x1)

                # phase 3: extend current inc c OR switch from dec b to inc c
                nc = max(c + x1, b + x1)

            elif x0 > x1:
                # phase 2: extend current dec b OR switch from inc a to dec b
                nb = max(b + x1, a + x1)

            ans = max(ans, nc)
            a, b, c = na, nb, nc

        return ans


ans = Solution().maxSumTrionic([0, -2, -1, -3, 0, 2, -1])
print(ans)

# 1390. Four Divisors

import math
from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans: int = 0

        for num in nums:
            div_count: int = 0
            in_sum: int = 0

            for divisor in range(1, int(math.sqrt(num)) + 1):
                if num % divisor == 0:
                    other: int = num // divisor

                    if divisor == other:
                        div_count += 1
                        in_sum += divisor
                    else:
                        div_count += 2
                        in_sum += divisor + other

                    if div_count > 4:
                        break

            if div_count == 4:
                ans += in_sum

        return ans


ans = Solution().sumFourDivisors([21, 4, 7])
print(ans)

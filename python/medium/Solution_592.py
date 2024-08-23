# 592. Fraction Addition and Subtraction

import re
from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums: list[int] = list(map(int, re.findall(r'[+-]?\d+', expression)))
        numerator: int = 0
        denominator: int = 1

        for i in range(0, len(nums), 2):
            num, den = nums[i], nums[i + 1]
            numerator = numerator * den + num * denominator
            denominator *= den

        common_divisor: int = gcd(numerator, denominator)

        return f"{numerator // common_divisor}/{denominator // common_divisor}"


ans = Solution().fractionAddition("-1/2+1/2+1/3")
print(ans)

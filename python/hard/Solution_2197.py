# 2197. Replace Non-Coprime Numbers in Array

from typing import List
from math import gcd


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack: list[int] = []

        for num in nums:
            stack.append(num)

            while len(stack) > 1:
                num1 = stack[-1]
                num2 = stack[-2]
                g: int = gcd(num1, num2)
                if g > 1:
                    lcm: int = (num1 // g) * num2
                    stack.pop()
                    stack.pop()
                    stack.append(lcm)
                else:
                    break
        return stack


ans = Solution().replaceNonCoprimes([6, 4, 3, 2, 7, 6, 2])
print(ans)

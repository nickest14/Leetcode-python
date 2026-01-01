# 66. Plus One

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry: int = 1
        for i in reversed(range(len(digits))):
            carry, digits[i] = divmod(digits[i] + carry, 10)
            if carry == 0:
                return digits
        return [1] + digits


ans = Solution().plusOne([1, 2, 9])
print(ans)

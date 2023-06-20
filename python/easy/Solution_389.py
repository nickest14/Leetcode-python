# 389. Find the Difference

import functools
import operator


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(functools.reduce(operator.xor, map(ord, s + t)))


ans = Solution().findTheDifference('abcd', 'abcde')
print(ans)

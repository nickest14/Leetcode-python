# 67. Add Binary

import itertools


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry, ans = 0, []
        for a, b in itertools.zip_longest(reversed(a), reversed(b), fillvalue='0'):
            carry, digit = divmod(int(a) + int(b) + carry, 2)
            ans.append(str(digit))
        return '1' * carry + ''.join(reversed(ans))


a = "11"
b = "1"
ans = Solution().addBinary(a, b)
print(ans)

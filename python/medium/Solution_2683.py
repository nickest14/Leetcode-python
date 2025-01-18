# 2683. Neighboring Bitwise XOR

from typing import List
from functools import reduce


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return reduce(lambda a, b: a ^ b, derived) == 0


ans = Solution().doesValidArrayExist([1, 1, 0])
print(ans)

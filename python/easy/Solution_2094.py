# 2094. Finding 3-Digit Even Numbers

from typing import List
from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counter: Counter = Counter(map(str, digits))
        return [v for v in range(100, 1000, 2) if Counter(str(v)) <= counter]


ans = Solution().findEvenNumbers([2, 1, 3, 0])
print(ans)

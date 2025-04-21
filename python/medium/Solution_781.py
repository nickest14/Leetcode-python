# 781. Rabbits in Forest


from typing import List
from collections import Counter
from math import ceil


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans: int = 0
        freq: dict[int, int] = Counter(answers)

        for k, v in freq.items():
            group_size: int = k + 1
            groups: int = ceil(v / group_size)
            ans += group_size * groups
        return ans


ans = Solution().numRabbits([1, 1, 2])
print(ans)

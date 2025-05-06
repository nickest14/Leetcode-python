# 1128. Number of Equivalent Domino Pairs


from typing import List
from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans: int = 0
        count: defaultdict[tuple[int, int], int] = defaultdict(int)
        for i, j in dominoes:
            count[1 << i | 1 << j] += 1

        for c in count.values():
            ans += c * (c - 1) // 2

        return ans


# ans = Solution().numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]])
ans = Solution().numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]])
print(ans)

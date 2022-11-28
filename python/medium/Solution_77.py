# 77. Combinations

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k:
            return [[]]
        ans = []
        for i in range(k, n + 1):
            for sublist in self.combine(i - 1, k - 1):
                ans.append(sublist + [i])
        return ans


n = 4
k = 2
ans = Solution().combine(n, k)
print(ans)

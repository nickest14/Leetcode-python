# 3577. Count the Number of Computer Unlocking Permutations

from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod: int = 10**9 + 7
        n: int = len(complexity)
        first: int = complexity[0]

        for i in range(1, n):
            if complexity[i] <= first:
                return 0

        ans: int = 1
        for i in range(2, n):
            ans = (ans * i) % mod

        return ans


ans = Solution().countPermutations([1, 2, 3])
print(ans)

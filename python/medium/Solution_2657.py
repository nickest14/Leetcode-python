# 2657. Find the Prefix Common Array of Two Arrays

from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n: int = len(A)
        ans: list[int] = [0] * n
        freq: list[int] = [0] * (n + 1)
        common: int = 0

        for i in range(n):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common += 1
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common += 1
            ans[i] = common

        return ans


ans = Solution().findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4])
print(ans)

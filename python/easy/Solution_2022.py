# 2022. Convert 1D Array Into 2D Array

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        ans: list[list[int]] = []
        for i in range(0, len(original), n):
            ans.append(original[i:i + n])

        return ans


ans = Solution().construct2DArray([1, 2, 3, 4], 2, 2)
print(ans)

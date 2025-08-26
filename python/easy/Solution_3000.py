# 3000. Maximum Area of Longest Diagonal Rectangle

from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area: int = 0
        max_diagonal: int = 0
        for x, y in dimensions:
            cur_diagonal: int = (x**2 + y**2)
            if cur_diagonal > max_diagonal or (cur_diagonal == max_diagonal and x * y > max_area):
                max_diagonal = cur_diagonal
                max_area = x * y
        return max_area


ans = Solution().areaOfMaxDiagonal([[9,3],[8,6]])
print(ans)

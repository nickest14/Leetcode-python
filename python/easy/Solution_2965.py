# 2965. Find Missing and Repeated Values

from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n: int = len(grid)
        nums_set = set()
        repeated: int = -1
        
        for row in grid:
            for num in row:
                if num in nums_set:
                    repeated = num
                nums_set.add(num)
        
        missing: int = next(num for num in range(1, n*n + 1) if num not in nums_set)
        
        return [repeated, missing]


ans = Solution().findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]])
print(ans)

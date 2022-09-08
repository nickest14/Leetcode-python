# 1886. Determine Whether Matrix Can Be Obtained By Rotation

from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]],
                     target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            # rotate next 90 degrees
            mat = [list(col) for col in zip(*mat[::-1])]
        return False


mat = [[0, 1], [1, 0]]
target = [[1, 0], [0, 1]]
ans = Solution().findRotation(mat, target)
print(ans)

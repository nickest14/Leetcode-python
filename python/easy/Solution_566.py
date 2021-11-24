# 566. Reshape the Matrix

import itertools
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        if row * col != r * c:
            return mat
        iter = itertools.chain(*mat)
        return [list(itertools.islice(iter, c)) for _ in range(r)]


ans = Solution().matrixReshape([[1, 2], [3, 4]], 1, 4)
print(ans)

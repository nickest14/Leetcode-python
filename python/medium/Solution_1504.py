# 1504. Count Submatrices With All Ones

from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        h: list[int] = [0] * c
        ans: int = 0
        for i in range(r):
            for j in range(c):
                h[j] = h[j] + 1 if mat[i][j] else 0

            sum_v: list[int] = [0] * c
            stack: list[int] = []
            for j in range(c):
                while stack and h[stack[-1]] >= h[j]:
                    stack.pop()
                if stack:
                    p = stack[-1]
                    sum_v[j] = sum_v[p] + h[j] * (j - p)
                else:
                    sum_v[j] = h[j] * (j + 1)
                stack.append(j)
                ans += sum_v[j]
        return ans


ans = Solution().numSubmat([[1, 0, 1], [1, 1, 0], [1, 1, 0]])
print(ans)

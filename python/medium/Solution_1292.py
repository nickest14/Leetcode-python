# 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m: int = len(mat)
        n: int = len(mat[0])

        prefix: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]
                )

        left: int = 0
        right: int = min(m, n)
        ans: int = 0

        while left <= right:
            mid = (left + right) // 2
            found = False
            for i in range(mid, m + 1):
                for j in range(mid, n + 1):
                    total = (
                        prefix[i][j]
                        - prefix[i - mid][j]
                        - prefix[i][j - mid]
                        + prefix[i - mid][j - mid]
                    )
                    if total <= threshold:
                        found = True
                        break
                if found:
                    break
            if found:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


ans = Solution().maxSideLength(
    [[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], 4
)
print(ans)

# 2579. Count Total Number of Colored Cells


class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1

        corner = n * (n - 1) // 2  # (1 + (n - 1)) * (n-1) / 2
        return (2 * n - 1) ** 2 - 4 * corner


ans = Solution().coloredCells(3)
print(ans)

# 1536. Minimum Swaps to Arrange a Binary Grid

from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n: int = len(grid)
        zeros: list[int] = []

        for row in grid:
            count: int = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            zeros.append(count)

        ans: int = 0
        for i in range(n):
            needed: int = n - i - 1
            j = i
            while j < n and zeros[j] < needed:
                j += 1
            if j == n:
                return -1
            while j > i:
                zeros[j], zeros[j - 1] = zeros[j - 1], zeros[j]
                j -= 1
                ans += 1

        return ans


ans = Solution().minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]])
print(ans)

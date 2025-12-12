# 3531. Count Covered Buildings

from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_max: list[int] = [0] * (n + 1)
        x_min: list[int] = [n + 1] * (n + 1)
        y_max: list[int] = [0] * (n + 1)
        y_min: list[int] = [n + 1] * (n + 1)

        for x, y in buildings:
            x_max[y] = max(x_max[y], x)
            x_min[y] = min(x_min[y], x)
            y_max[x] = max(y_max[x], y)
            y_min[x] = min(y_min[x], y)

        ans: int = 0
        for x, y in buildings:
            if x_min[y] < x < x_max[y] and y_min[x] < y < y_max[x]:
                ans += 1

        return ans


ans = Solution().countCoveredBuildings(3, [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]])
print(ans)

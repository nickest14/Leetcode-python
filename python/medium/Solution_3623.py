# 3623. Count Number of Trapezoids I

from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod: int = 10**9 + 7
        dic: dict[int, int] = {}
        for x, y in points:
            dic[y] = dic.get(y, 0) + 1
        seg: list[int] = []
        for k in dic.values():
            if k >= 2:
                seg.append((k * (k - 1) // 2) % mod)
        s: int = 0
        ans: int = 0
        for v in seg:
            ans = (ans + v * s) % mod
            s = (s + v) % mod
        return ans


ans = Solution().countTrapezoids([[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]])
print(ans)

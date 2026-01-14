# 3454. Separate Squares II

from collections import Counter
from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events: list[tuple[float, int, float, float]] = []
        for x, y, side_len in squares:
            events.append((y, 1, x, x + side_len))
            events.append((y + side_len, -1, x, x + side_len))

        events.sort()
        xs: Counter[tuple[float, float], int] = Counter()
        prev_y = events[0][0]
        total: float = 0.0
        areas: list[tuple[float, float, float]] = []

        def union_len():
            intervals = sorted(xs.keys())
            if not intervals:
                return 0.0
            res: float = 0.0
            end: float = intervals[0][0]
            for a, b in intervals:
                if a > end:
                    res += b - a
                    end = b
                elif b > end:
                    res += b - end
                    end = b
            return res

        for y, typ, x1, x2 in events:
            if y > prev_y and xs:
                h = y - prev_y
                w = union_len()
                areas.append((prev_y, h, w))
                total += h * w
            if typ == 1:
                xs[(x1, x2)] += 1
            else:
                xs[(x1, x2)] -= 1
                if xs[(x1, x2)] == 0:
                    del xs[(x1, x2)]
            prev_y = y

        half = total / 2
        acc = 0
        for y, h, w in areas:
            if acc + h * w >= half:
                return y + (half - acc) / w
            acc += h * w

        return 0.0


ans = Solution().separateSquares([[0, 0, 1], [2, 2, 1]])
print(ans)

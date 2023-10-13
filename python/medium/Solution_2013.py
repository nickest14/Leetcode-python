# 2013. Detect Squares

from typing import List
from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.pts_count = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.pts_count[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        ans = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            ans += self.pts_count[(x, py)] * self.pts_count[(px, y)]
        return ans


# Your DetectSquares object will be instantiated and called as such:
obj = DetectSquares()
obj.add([3, 10])
obj.add([11, 2])
obj.add([3, 2])
print(obj.count([11, 10]))  # 1
print(obj.count([14, 8]))  # 0
obj.add([11, 2])
print(obj.count([11, 10]))  # 2

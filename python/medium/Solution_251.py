# 251. Flatten 2D Vector

from typing import List


class Vector2D:
    def __init__(self, v: List[List[int]]):
        self.v = [i for row in reversed(v) for i in reversed(row)]

    def next(self) -> int:
        return self.v.pop()

    def hasNext(self) -> bool:
        return self.v is not None


# Your Vector2D object will be instantiated and called as such:
obj = Vector2D([[1, 2], [3], [4, 5, 6]])
param_1 = obj.next()
param_2 = obj.hasNext()
print(f'{param_1=} {param_2=}')

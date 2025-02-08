# 2349. Design a Number Container System

import heapq
from collections import defaultdict


class NumberContainers:
    def __init__(self):
        self.index_num: dict[int, int] = {}
        self.num_to_indices: dict[int, list[int]] = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.index_num[index] = number
        heapq.heappush(self.num_to_indices[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_to_indices:
            return -1

        pos_indices = self.num_to_indices[number]
        while pos_indices:
            min_index = pos_indices[0]
            if self.index_num[min_index] == number:
                return min_index

            heapq.heappop(pos_indices)  # invalid index, new num at index

        return -1


ans: list[int] = []
obj = NumberContainers()
ans.append(obj.find(10))
ans.append(obj.change(2, 50))
ans.append(obj.find(50))
ans.append(obj.change(2, 10))
ans.append(obj.find(10))
ans.append(obj.change(1, 10))
ans.append(obj.change(3, 10))
ans.append(obj.find(10))
print(ans)

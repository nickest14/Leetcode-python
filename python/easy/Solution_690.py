# 690. Employee Importance

from typing import List


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(eid: int) -> int:
            return lookup[eid].importance + sum(map(dfs, lookup[eid].subordinates))

        # # bfs solution
        # import collections
        # def bfs(eid: int) -> int:
        #     queue = collections.deque([lookup[eid]])
        #     total = 0
        #     while queue:
        #         e = queue.popleft()
        #         total += e.importance
        #         queue += map(lookup.get, e.subordinates)
        #     return total

        lookup = {e.id: e for e in employees}
        return dfs(id)


e1 = Employee(1, 5, [2, 3])
e2 = Employee(2, 3, [])
e3 = Employee(3, 3, [])

ans = Solution().getImportance([e1, e2, e3], 1)
print(ans)

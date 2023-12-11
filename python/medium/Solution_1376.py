# 1376. Time Needed to Inform All Employees

from collections import defaultdict, deque
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)  # manager -> [list of employes]
        for i in range(n):
            adj[manager[i]].append(i)

        # bfs
        q = deque([(headID, 0)])  # (id, time)
        ans = 0
        while q:
            i, time = q.popleft()
            ans = max(ans, time)
            for emp in adj[i]:
                q.append((emp, time + informTime[i]))

        return ans


ans = Solution().numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0])
print(ans)

# 2045. Second Minimum Time to Reach Destination

from typing import List
from collections import defaultdict
import heapq


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph: dict[list] = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q: list = []
        heapq.heappush(q, (0, 1))  # (time, node)
        unique_visit: list[int] = [0] * (n + 1)
        distance = [-1] * (n + 1)

        while q:
            t, node = heapq.heappop(q)
            if distance[node] == t or unique_visit[node] >= 2:
                continue
            unique_visit[node] += 1
            distance[node] = t
            if node == n and unique_visit[node] == 2:
                return distance[node]

            if (t // change) % 2 != 0:
                t = (t // change + 1) * change
            for neighbor in graph[node]:
                heapq.heappush(q, (t + time, neighbor))

        return -1


n = 5
edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
time = 3
change = 5
ans = Solution().secondMinimum(n, edges, time, change)
print(ans)

# n = 2
# edges = [[1, 2]]
# time = 3
# change = 2
# ans = Solution().secondMinimum(n, edges, time, change)
# print(ans)

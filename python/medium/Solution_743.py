# 743. Network Delay Time

import collections
import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        heap = [(k, 0)]
        dist = {k: 0}
        graph = collections.defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w
        while heap:
            u, cost = heapq.heappop(heap)
            if cost > dist[u]:
                continue
            for v, w in graph[u].items():
                if dist[u] + w < dist.get(v, float('inf')):
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (v, dist[v]))
        ans = max(dist.get(i, float('inf')) for i in range(1, n + 1))
        return ans if ans < float('inf') else -1


times = [[2, 1, 3], [2, 3, 2], [3, 4, 5]]
n = 4
k = 2
ans = Solution().networkDelayTime(times, n, k)
print(ans)

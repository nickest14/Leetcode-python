# 1976. Number of Ways to Arrive at Destination

from typing import List
from heapq import heappop, heappush


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph: list[list[tuple[int]]] = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        dist: list[int] = [float("inf")] * n
        ways: list[int] = [0] * n
        dist[0] = 0
        ways[0] = 1
        pq: list[tuple[int]] = [(0, 0)]
        mod = 10**9 + 7

        # Dijkstra's algorithm
        while pq:
            d, node = heappop(pq)
            if d > dist[node]:
                continue
            for neighbor, time in graph[node]:
                if dist[node] + time < dist[neighbor]:
                    dist[neighbor] = dist[node] + time
                    ways[neighbor] = ways[node]
                    heappush(pq, (dist[neighbor], neighbor))
                elif dist[node] + time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % mod

        return ways[n - 1]


ans = Solution().countPaths(
    7,
    [
        [0, 6, 7],
        [0, 1, 2],
        [1, 2, 3],
        [1, 3, 3],
        [6, 3, 3],
        [3, 5, 1],
        [6, 5, 1],
        [2, 5, 1],
        [0, 4, 5],
        [4, 6, 2],
    ],
)
print(ans)

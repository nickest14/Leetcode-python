# 1514. Path with Maximum Probability


from typing import List
import heapq
import collections


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(dict)
        dist, heap = {start: -1}, [(-1, start)]
        for (u, v), p in zip(edges, succProb):
            graph[u][v] = graph[v][u] = p
        while heap:
            prob, u = heapq.heappop(heap)
            if prob > dist[u]:
                continue
            if u == end:
                return -prob
            for v, p in graph[u].items():
                if dist[u] * p < dist.get(v, float('inf')):
                    dist[v] = dist[u] * p
                    # due to heap is sort by min to max
                    heapq.heappush(heap, (dist[v], v))
        return 0


n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start = 0
end = 2
ans = Solution().maxProbability(n, edges, succProb, start, end)
print(ans)


# lookup = {sum(d > distanceThreshold for d in row): i for i, row in enumerate(matrix)}

# lookup = {}
# for i, row in enumerate(matrix):
#     count = 0
#     for d in row:
#         if d > distanceThreshold:
#             count += 1
#     lookup[count] = i

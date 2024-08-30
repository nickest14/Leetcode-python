# 2699. Modify Graph Edge Weights

from typing import List
import heapq


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        adjs: list[dict[int, dict[int, int]]] = [{} for _ in range(n)]
        for (s, d, w) in edges:
            adjs[s][d] = w
            adjs[d][s] = w

        dist: list[int] = [float('inf')] * n
        dist[source] = 0

        pq: list[tuple[int, int]] = [(0, source)]  # (distance, node)
        heapq.heapify(pq)
        self.dijkstra(adjs, dist, pq)

        if dist[destination] == target:
            return self.fill(edges)
        elif dist[destination] < target:
            return []

        for edge in edges:
            if edge[2] == -1:
                edge[2] = 1
                adjs[edge[0]][edge[1]] = 1
                adjs[edge[1]][edge[0]] = 1

                pq = [(dist[edge[0]], edge[0]), (dist[edge[1]], edge[1])]

                self.dijkstra(adjs, dist, pq)

                if dist[destination] == target:
                    return self.fill(edges)
                elif dist[destination] < target:
                    edge[2] += target - dist[destination]
                    adjs[edge[0]][edge[1]] = edge[2]
                    adjs[edge[1]][edge[0]] = edge[2]
                    return self.fill(edges)

        return []

    def fill(self, edges: List[List[int]]):
        for edge in edges:
            if edge[2] == -1:
                edge[2] = int(2e9)
        return edges

    def dijkstra(self, adjs: list[dict[int, dict[int, int]]], dist: list[int], pq: list[tuple[int, int]]):
        while pq:
            _, cur = heapq.heappop(pq)
            for next_node, weight in adjs[cur].items():
                if weight > 0:
                    new_dist: int = dist[cur] + weight
                    if dist[next_node] > new_dist:
                        dist[next_node] = new_dist
                        heapq.heappush(pq, (new_dist, next_node))


n = 5
edges = [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]]
source = 0
destination = 1
target = 5
ans = Solution().modifiedGraphEdges(n, edges, source, destination, target)
print(ans)


# n = 4
# edges = [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]]
# source = 0
# destination = 2
# target = 6
# ans = Solution().modifiedGraphEdges(n, edges, source, destination, target)
# print(ans)

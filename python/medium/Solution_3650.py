# 3185. Count Pairs That Form a Complete Day II

from typing import List
from heapq import heappop, heappush
from collections import defaultdict


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
        for source, target, weight in edges:
            graph[source].append((target, weight))
            graph[target].append((source, weight * 2))

        min_costs: list[float] = [float("inf")] * n
        min_costs[0] = 0

        priority_queue: list[tuple[float, int]] = [(0, 0)]
        while priority_queue:
            current_cost, current_node = heappop(priority_queue)

            if current_cost > min_costs[current_node]:
                continue

            if current_node == n - 1:
                return int(current_cost)

            for neighbor, edge_weight in graph[current_node]:
                new_cost = current_cost + edge_weight
                if new_cost < min_costs[neighbor]:
                    min_costs[neighbor] = new_cost
                    heappush(priority_queue, (new_cost, neighbor))

        return -1


ans = Solution().minCost(4, [[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]])
print(ans)

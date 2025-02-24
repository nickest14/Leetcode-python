# 2467. Most Profitable Path in a Tree

from typing import List
from collections import defaultdict


class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        graph: dict[int, list] = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        bob_path: list[int] = [-1] * len(amount)
        path: list[int] = []

        def fill_bob_path(node: int, parent: int):
            if node == 0:
                return True
            for neighbor in graph[node]:
                if neighbor != parent:
                    path.append(node)
                    if fill_bob_path(neighbor, node):
                        return True
                    path.pop()

        fill_bob_path(bob, -1)
        for i, node in enumerate(path):
            bob_path[node] = i

        def get_alice_max_score(node: int, parent: int, currScore: int, timestamp: int):
            if bob_path[node] == -1 or bob_path[node] > timestamp:
                currScore += amount[node]
            elif bob_path[node] == timestamp:
                currScore += amount[node] // 2
            return (
                currScore
                if len(graph[node]) == 1 and node != 0
                else max(
                    get_alice_max_score(neighbor, node, currScore, timestamp + 1)
                    for neighbor in graph[node]
                    if neighbor != parent
                )
            )

        return get_alice_max_score(0, -1, 0, 0)


ans = Solution().mostProfitablePath(
    [[0, 1], [1, 2], [1, 3], [3, 4]], 3, [-2, 4, 2, -4, 6]
)
print(ans)

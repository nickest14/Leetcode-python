# 3373. Maximize the Number of Target Nodes After Connecting Trees II

from typing import List, Tuple
from collections import deque


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        def bfs(graph: List[List[int]]) -> Tuple[List[int], List[int]]:
            n: int = len(graph)
            color_count: List[int] = [0, 0]
            node_color: List[int] = [0] * n
            visited: List[bool] = [False] * n
            queue: deque[Tuple[int, int]] = deque([(0, 0)])
            visited[0] = True

            while queue:
                node, color = queue.popleft()
                node_color[node] = color
                color_count[color] += 1

                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, 1 - color))

            return color_count, node_color

        n1: int = len(edges1) + 1
        n2: int = len(edges2) + 1
        adj1: List[List[int]] = [[] for _ in range(n1)]
        adj2: List[List[int]] = [[] for _ in range(n2)]

        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        color1, node_color1 = bfs(adj1)
        color2, _ = bfs(adj2)

        max_color2 = max(color2)

        ans: List[int] = [0] * n1
        for i in range(n1):
            ans[i] = color1[node_color1[i]] + max_color2

        return ans


ans = Solution().maxTargetNodes(
    [[0, 1], [0, 2], [2, 3], [2, 4]],
    [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
)
print(ans)

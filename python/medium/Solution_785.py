# 785. Is Graph Bipartite?

from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(u: int, color: int) -> bool:
            if u in colors:
                return colors[u] == color
            colors[u] = color
            return all(dfs(v, color ^ 1) for v in graph[u])

        colors = {}
        return all(dfs(u, 1) for u in range(len(graph)) if u not in colors)

    # # bfs
    # def isBipartite(self, graph: List[List[int]]) -> bool:
    #     import collections
    #     colors = {}
    #     for i in range(len(graph)):
    #         if i in colors:
    #             continue
    #         color = 1
    #         queue = collections.deque([i])
    #         while queue:
    #             for _ in range(len(queue)):
    #                 node = queue.popleft()
    #                 if node in colors:
    #                     if colors[node] != color:
    #                         return False
    #                 else:
    #                     colors[node] = color
    #                     queue += graph[node]
    #             color ^= 1
    #     return True


graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
# graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
ans = Solution().isBipartite(graph)
print(ans)

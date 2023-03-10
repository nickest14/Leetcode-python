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


graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
# graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
ans = Solution().isBipartite(graph)
print(ans)

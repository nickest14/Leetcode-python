# 684. Redundant Connection

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(i: int) -> int:
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(x: int, y: int):
            px, py = map(find, (x, y))
            if px == py:
                return
            if rank[x] > rank[y]:
                px, py = py, px
            parent[px] = py
            rank[py] += rank[px] == rank[py]

        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        for edge in edges:
            px, py = map(find, edge)
            if px == py:
                return edge
            union(px, py)


# edges = [[1, 2], [1, 3], [2, 3]]
edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
ans = Solution().findRedundantConnection(edges)
print(ans)

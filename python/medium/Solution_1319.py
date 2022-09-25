# 1319. Number of Operations to Make Network Connected

from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(*pair):
            px, py = map(find, pair)
            if px != py:
                if rank[px] < rank[py]:
                    px, py = py, px
                parent[px] = py
                if rank[px] == rank[py]:
                    rank[py] += 1

        if len(connections) < n - 1:
            return -1
        parent = list(range(n))
        rank = [0] * n
        for u, v in connections:
            union(u, v)
        return len(set(map(find, parent))) - 1


n = 6
connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
ans = Solution().makeConnected(n, connections)
print(ans)

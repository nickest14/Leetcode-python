# 547. Number of Provinces

from typing import List


class Solution:
    # dsu
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(*pair) -> None:
            px, py = map(find, pair)
            if px != py:
                if rank[px] > rank[py]:
                    px, py = py, px
                parent[px] = py
                if rank[px] == rank[py]:
                    rank[py] += 1

        n = len(isConnected)
        parent, rank = list(range(n)), [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)
        return len(set(find(i) for i in range(n)))

# class Solution:
#     # dfs
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         ans = 0
#         seen = set()

#         def dfs(i):
#             seen.add(i)
#             for j, connected in enumerate(isConnected[i]):
#                 if connected and j not in seen:
#                     dfs(j)

#         node_count = len(isConnected)
#         for i in range(node_count):
#             if i not in seen:
#                 dfs(i)
#                 ans += 1
#         return ans


# class Solution:
#     # bfs
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         ans = 0
#         seen = set()

#         def bfs(i: int) -> None:
#             queue = collections.deque([i])
#             while queue:
#                 node = queue.popleft()
#                 seen.add(node)
#                 for j, connected in enumerate(isConnected[node]):
#                     if connected and j not in seen:
#                         queue.append(j)

#         node_count = len(isConnected)
#         for i in range(node_count):
#             if i not in seen:
#                 bfs(i)
#                 ans += 1
#         return ans


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
ans = Solution().findCircleNum(isConnected)
print(ans)

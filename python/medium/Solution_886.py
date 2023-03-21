# 886. Possible Bipartition


from typing import List
import collections


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node: int, color: int):
            if node in colors:
                return colors[node] == color
            colors[node] = color
            check_neighbor = []
            for neighbor in graph[node]:
                check_neighbor.append(dfs(neighbor, color ^ 1))
            return all(check_neighbor)

        graph, colors = collections.defaultdict(list), {}
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        check_nodes = []
        for node in range(1, n + 1):
            if node not in colors:
                check_nodes.append(dfs(node, 0))
        return all(check_nodes)

    # # bfs
    # def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
    #     graph, colors = collections.defaultdict(list), {}
    #     for u, v in dislikes:
    #         graph[u].append(v)
    #         graph[v].append(u)
    #     for i in range(1, n + 1):
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


n = 5
dislikes = [[1, 2], [1, 3], [2, 4], [2, 5]]
ans = Solution().possibleBipartition(n, dislikes)
print(ans)

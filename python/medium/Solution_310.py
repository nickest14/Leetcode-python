# 310. Minimum Height Trees

from typing import List
import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 2:
            return list(range(n))
        graph = collections.defaultdict(list)
        in_degree = [0] * n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            in_degree[a] += 1
            in_degree[b] += 1
        queue = collections.deque(i for i, d in enumerate(in_degree) if d == 1)
        rest = n
        while rest > 2:
            for _ in range(len(queue)):
                node = queue.popleft()
                for nei in graph[node]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 1:
                        queue.append(nei)
                in_degree[node] = 0
                rest -= 1
        return list(queue)


n = 4
edges = [[1, 0], [1, 2], [1, 3]]
ans = Solution().findMinHeightTrees(n, edges)
print(ans)


# # Time Limit Exceeded
# import functools

# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         @functools.lru_cache
#         def height(node: int, prev: int = -1) -> int:
#             return max((height(n, node) for n in graph[node] if n != prev), default=0) + 1

#         graph = collections.defaultdict(list)
#         for a, b in edges:
#             graph[a].append(b)
#             graph[b].append(a)
#         mh, result = n, []
#         for i in range(n):
#             h = height(i)
#             if h < mh:
#                 mh = h
#                 result = [i]
#             elif h == mh:
#                 result.append(i)
#         return result
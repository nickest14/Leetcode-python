# 2493. Divide Nodes Into the Maximum Number of Groups

from typing import List
from collections import deque, defaultdict


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        group: list[list[int]] = [[] for _ in range(n)]
        for a, b in edges:
            group[a - 1].append(b - 1)
            group[b - 1].append(a - 1)

        dic = defaultdict(int)
        for i in range(n):
            q: list[int] = deque([i])
            dist: list[int] = [0] * n
            dist[i] = mx = 1
            root = i
            while q:
                a = q.popleft()
                root = min(root, a)
                for b in group[a]:
                    if dist[b] == 0:
                        dist[b] = dist[a] + 1
                        mx = max(mx, dist[b])
                        q.append(b)
                    elif abs(dist[b] - dist[a]) != 1:
                        return -1
            dic[root] = max(dic[root], mx)
        return sum(dic.values())


ans = Solution().magnificentSets(6, [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]])
# ans = Solution().magnificentSets(3, [[1,2],[2,3],[3,1]])
# ans = Solution().magnificentSets(
#     92,
#     [
#         [67, 29],
#         [13, 29],
#         [77, 29],
#         [36, 29],
#         [82, 29],
#         [54, 29],
#         [57, 29],
#         [53, 29],
#         [68, 29],
#         [26, 29],
#         [21, 29],
#         [46, 29],
#         [41, 29],
#         [45, 29],
#         [56, 29],
#         [88, 29],
#         [2, 29],
#         [7, 29],
#         [5, 29],
#         [16, 29],
#         [37, 29],
#         [50, 29],
#         [79, 29],
#         [91, 29],
#         [48, 29],
#         [87, 29],
#         [25, 29],
#         [80, 29],
#         [71, 29],
#         [9, 29],
#         [78, 29],
#         [33, 29],
#         [4, 29],
#         [44, 29],
#         [72, 29],
#         [65, 29],
#         [61, 29],
#     ],
# )
print(ans)

# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance


from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[0 if i == j else float('inf') for i in range(n)] for j in range(n)]
        for u, v, w in edges:
            matrix[u][v] = matrix[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        lookup = {sum(d > distanceThreshold for d in row): i for i, row in enumerate(matrix)}
        return lookup[max(lookup.keys())]


n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4
ans = Solution().findTheCity(n, edges, distanceThreshold)
print(ans)


# lookup = {sum(d > distanceThreshold for d in row): i for i, row in enumerate(matrix)}

# lookup = {}
# for i, row in enumerate(matrix):
#     count = 0
#     for d in row:
#         if d > distanceThreshold:
#             count += 1
#     lookup[count] = i

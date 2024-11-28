# 3243. Shortest Distance After Road Addition Queries I


from typing import List


class Solution:

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def update_distance(current: int):
            new_dist = distances[current] + 1
            for neighbor in graph[current]:
                if distances[neighbor] <= new_dist:
                    continue
                distances[neighbor] = new_dist
                update_distance(neighbor)

        distances: list[int] = [n - 1 - i for i in range(n)]
        graph: list[list[int]] = [[] for _ in range(n)]
        for i in range(n - 1):
            graph[i + 1].append(i)

        ans: list[int] = []
        for source, target in queries:
            graph[target].append(source)
            distances[source] = min(distances[source], distances[target] + 1)
            update_distance(source)
            ans.append(distances[0])

        return ans


ans = Solution().shortestDistanceAfterQueries(5, [[2, 4], [0, 2], [0, 4]])
print(ans)

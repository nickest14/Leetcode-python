# 210. Course Schedule II

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(vertex: int):
            if status[vertex] > -1:
                return status[vertex]
            status[vertex] = 0
            for dest in graph[vertex]:
                if not dfs(dest):
                    return False
            status[vertex] = 1
            result.append(vertex)
            return True

        graph = [[] for _ in range(numCourses)]
        status = [-1] * numCourses
        result = []
        for course, prev in prerequisites:
            graph[prev].append(course)
        for vertex in range(numCourses):
            if status[vertex] == -1 and not dfs(vertex):
                return []
        return result[::-1]


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
ans = Solution().findOrder(numCourses, prerequisites)
print(ans)

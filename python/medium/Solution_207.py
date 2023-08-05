# 207. Course Schedule

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        pre_dict = {i: [] for i in range(numCourses)}
        for cur, pre in prerequisites:
            pre_dict[cur].append(pre)
        visiting = set()

        def dfs(cur):
            if cur in visiting:
                return False
            if not pre_dict[cur]:
                return True
            visiting.add(cur)
            for pre in pre_dict[cur]:
                if not dfs(pre):
                    return False
            visiting.remove(cur)
            pre_dict[cur] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(vertex: int) -> bool:
            if status[vertex] > -1:
                return status[vertex]
            status[vertex] = 0
            for dest in graph[vertex]:
                if not dfs(dest):
                    return False
            status[vertex] = 1
            return True

        graph = [[] for _ in range(numCourses)]
        status = [-1] * numCourses
        for course, prev in prerequisites:
            graph[prev].append(course)
        for vertex in range(numCourses):
            if status[vertex] == -1 and not dfs(vertex):
                return False
        return True


numCourses = 5
prerequisites = [[0, 1], [0, 2], [0, 3], [3, 2], [0, 4], [1, 4]]
# prerequisites = [[0, 1], [0, 2], [0, 3], [3, 2], [4, 0], [1, 4]]
ans = Solution().canFinish(numCourses, prerequisites)
print(ans)

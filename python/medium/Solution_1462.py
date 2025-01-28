# 1462. Course Schedule IV

from typing import List
from collections import defaultdict


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        prereq_map: dict[int, list[int]] = defaultdict(list)
        for prereq in prerequisites:
            prereq_map[prereq[1]].append(prereq[0])

        memo: dict[int, bool] = {}

        def dfs(course: int, prereq: int) -> bool:
            if (course, prereq) in memo:
                return memo[(course, prereq)]
            course_prereqs = prereq_map[course]
            for p in course_prereqs:
                if p == prereq or dfs(p, prereq):
                    memo[(course, prereq)] = True
                    return True

            memo[(course, prereq)] = False
            return False

        return [dfs(query[1], query[0]) for query in queries]


ans = Solution().checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]])
print(ans)

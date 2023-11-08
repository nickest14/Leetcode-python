# 802. Find Eventual Safe States

from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}

        def dfs(i: int):
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return safe[i]
            safe[i] = True
            return True

        ans = []
        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans


ans = Solution().eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []])
print(ans)

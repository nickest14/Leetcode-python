# 2685. Count the Number of Complete Components

from typing import List
from collections import defaultdict


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph: dict[list] = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        ans: int = 0

        def dfs(node: int, component: set):
            component.add(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for i in range(n):
            if i not in visited:
                component = set()
                dfs(i, component)
                if all(len(graph[node]) == len(component) - 1 for node in component):
                    ans += 1
        return ans


ans = Solution().countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]])
# ans = Solution().countCompleteComponents(3, [[1,0],[2,1]])
print(ans)

# 2392. Build a Matrix With Conditions

from typing import List
from collections import defaultdict


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src: int, graph: dict[list], visited: set[int], cur_path: set[int], ans: list[int]):
            if src in cur_path:
                return False  # cycle detected
            if src in visited:
                return True

            visited.add(src)
            cur_path.add(src)

            for neighbor in graph[src]:
                if not dfs(neighbor, graph, visited, cur_path, ans):
                    return False

            cur_path.remove(src)
            ans.append(src)
            return True

        def topo_sort(edges: list[list[int]]) -> list[int]:
            graph: dict[list] = defaultdict(list)
            for src, dist in edges:
                graph[src].append(dist)

            visited: set[int] = set()
            cur_path: set[int] = set()
            ans: list[int] = []

            for src in range(1, k + 1):
                if not dfs(src, graph, visited, cur_path, ans):
                    return []
            return ans[::-1]

        row_sorting: list[int] = topo_sort(rowConditions)
        col_sorting: list[int] = topo_sort(colConditions)
        if not row_sorting or not col_sorting:
            return []

        value_postion: dict[int, list[int]] = {
            n: [0, 0] for n in range(1, k + 1)
        }
        for ind, val in enumerate(row_sorting):
            value_postion[val][0] = ind
        for ind, val in enumerate(col_sorting):
            value_postion[val][1] = ind

        ans: list[list[int]] = [[0 for _ in range(k)] for _ in range(k)]
        for value in range(1, k + 1):
            row, col = value_postion[value]
            ans[row][col] = value
        return ans


# k = 3
# rowConditions = [[1, 2], [3, 2]]
# colConditions = [[2, 1], [3, 2]]

k = 3
rowConditions = [[1, 2], [2, 3], [3, 1], [2, 3]]
colConditions = [[2, 1]]

ans = Solution().buildMatrix(k, rowConditions, colConditions)
print(ans)

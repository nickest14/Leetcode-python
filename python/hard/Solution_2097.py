# 2097. Valid Arrangement of Pairs

from typing import List
from collections import defaultdict, deque


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        for start, end in pairs:
            graph[start].append(end)
            in_degree[end] += 1
            out_degree[start] += 1

        start_node: int = pairs[0][0]
        for node in graph:
            if out_degree[node] > in_degree[node]:
                start_node = node
                break

        stack: list[int] = [start_node]
        nodes = []
        while stack:
            while graph[stack[-1]]:
                next_node = graph[stack[-1]].popleft()
                stack.append(next_node)
            nodes.append(stack.pop())

        nodes.reverse()
        return [[nodes[i], nodes[i + 1]] for i in range(len(nodes) - 1)]


ans = Solution().validArrangement([[5, 1], [4, 5], [11, 9], [9, 4]])
print(ans)

# 3203. Find Minimum Diameter After Merging Two Trees

from collections import defaultdict
from math import ceil
from typing import List
from heapq import heappush, heappop


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def build_adj(edges: list[list[int]]):
            adj = defaultdict(list)
            for n1, n2 in edges:
                adj[n1].append(n2)
                adj[n2].append(n1)
            return adj

        adj1 = build_adj(edges1)
        adj2 = build_adj(edges2)

        # dfs, return [diam, max_leaf_path]
        def get_diameter(current, parent, adj) -> list[int]:
            max_d = 0
            max_child_paths = [0, 0]  # Only need to check two paths

            for neighbor in adj[current]:
                if neighbor == parent:
                    continue
                neighbor_d, neighbor_max_leaf_path = get_diameter(neighbor, current, adj)
                max_d = max(max_d, neighbor_d)

                heappush(max_child_paths, neighbor_max_leaf_path)
                heappop(max_child_paths)

            max_d = max(max_d, sum(max_child_paths))
            return [max_d, 1 + max(max_child_paths)]

        d1, _ = get_diameter(0, -1, adj1)
        d2, _ = get_diameter(0, -1, adj2)

        return max(d1, d2, 1 + ceil(d1 / 2) + ceil(d2 / 2))


ans = Solution().minimumDiameterAfterMerge([[0, 1], [0, 2], [0, 3]], [[0, 1]])
# ans = Solution().minimumDiameterAfterMerge([[0, 1], [1, 2], [2, 3], [3, 4], [0, 5], [5, 6]], [[0, 7]])
print(ans)

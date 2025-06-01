# 2359. Find Closest Node to Given Two Nodes

from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n: int = len(edges)

        def dist_to_node(node: int) -> list[int]:
            dist: list[int] = [-1] * n
            current: int = node
            distance: int = 0
            while current != -1 and dist[current] == -1:
                dist[current] = distance
                distance += 1
                current = edges[current]
            return dist

        dist1 = dist_to_node(node1)
        dist2 = dist_to_node(node2)

        min_max = float("inf")
        ans: int = -1
        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                current_max = max(dist1[i], dist2[i])
                if current_max < min_max:
                    min_max = current_max
                    ans = i

        return ans


ans = Solution().closestMeetingNode([2, 2, 3, -1], 0, 1)
print(ans)

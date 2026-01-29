# 2976. Minimum Cost to Convert String I

from typing import List
from heapq import heappop, heappush


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        graph: list[list[tuple[int, int]]] = [[] for _ in range(26)]
        for a, b, c in zip(original, changed, cost):
            x: int = ord(a) - ord("a")
            y: int = ord(b) - ord("a")
            graph[x].append((y, c))

        def dijkstra(start: int) -> list[int]:
            dist: list[int] = [float("inf")] * 26
            dist[start] = 0
            pq: list[tuple[int, int]] = [(0, start)]
            while pq:
                d, u = heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in graph[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heappush(pq, (nd, v))
            return dist

        compute: list[list[int]] = [dijkstra(i) for i in range(26)]
        ans: int = 0
        for s, t in zip(source, target):
            si = ord(s) - ord("a")
            ti = ord(t) - ord("a")
            d: int = compute[si][ti]
            if d >= float("inf"):
                return -1
            ans += d
        return ans


source = "abcd"
target = "acbe"
original = ["a", "b", "c", "c", "e", "d"]
changed = ["b", "c", "b", "e", "b", "e"]
cost = [2, 5, 5, 1, 2, 20]
ans = Solution().minimumCost(source, target, original, changed, cost)
print(ans)

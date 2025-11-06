# 3607. Power Grid Maintenance

from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        parents: list[int] = [i for i in range(c + 1)]
        online_status: list[bool] = [True] * (c + 1)

        def find(x: int) -> int:
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(u: int, v: int) -> None:
            pu, pv = find(u), find(v)
            if pu != pv:
                if pu <= pv:
                    parents[pv] = pu
                else:
                    parents[pu] = pv

        for u, v in connections:
            union(u, v)

        min_in_component: defaultdict[int, list[int]] = defaultdict(list)

        for i in range(c + 1):
            heappush(min_in_component[find(i)], i)

        ans: list[int] = []
        for op, x in queries:
            if op == 2:
                online_status[x] = False
            else:
                if online_status[x]:
                    ans.append(x)
                else:
                    min_in_component_heap, notFound = min_in_component[find(x)], True
                    while min_in_component_heap:
                        station: int = min_in_component_heap[0]
                        if online_status[station]:
                            ans.append(station)
                            notFound = False
                            break
                        heappop(min_in_component_heap)
                    if notFound:
                        ans.append(-1)

        return ans


ans = Solution().processQueries(
    c=5,
    connections=[[1, 2], [2, 3], [3, 4], [4, 5]],
    queries=[[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]],
)
print(ans)

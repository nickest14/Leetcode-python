# 1722. Minimize Hamming Distance After Swap Operations

from typing import List
import collections


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int],
                               allowedSwaps: List[List[int]]) -> int:
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(*pair):
            px, py = map(find, pair)
            if px != py:
                if rank[px] < rank[py]:
                    px, py = py, px
                parent[px] = py
                if rank[px] == rank[py]:
                    rank[py] += 1
        n = len(source)
        parent, rank = list(range(n)), [0] * n
        counters = collections.defaultdict(collections.Counter)
        for i, j in allowedSwaps:
            union(i, j)
        for i, (s, t) in enumerate(zip(source, target)):
            p = find(i)
            counters[p][s] += 1
            counters[p][t] -= 1
        ans = 0
        for counter in counters.values():
            for count in counter.values():
                if count > 0:
                    ans += count
        return ans


# source = [1, 2, 3, 4]
# target = [2, 1, 4, 5]
# allowedSwaps = [[0, 1], [2, 3]]
source = [7, 8, 9, 2]
target = [11, 10, 8, 2]
# allowedSwaps = [[1, 2], [1, 3], [0, 3]]
allowedSwaps = [[1, 2]]
ans = Solution().minimumHammingDistance(source, target, allowedSwaps)
print(ans)

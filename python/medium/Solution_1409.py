# 1409. Queries on a Permutation With Key

from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        def update(i: int, delta: int):
            while i <= 2 * m + 1:
                BIT[i] += delta
                i += i & -i

        def presum(i: int) -> int:
            total = 0
            while i > 0:
                total += BIT[i]
                i -= i & -i
            return total

        BIT, lookup = [0] * (2 * m + 1), {}
        for i in range(1, m + 1):
            lookup[i] = i + m
            update(i + m, 1)

        ans, tail = [], m
        for query in queries:
            idx = lookup.pop(query)
            ans.append(presum(idx - 1))
            update(idx, -1)
            update(tail, 1)
            lookup[query] = tail
            tail -= 1
        return ans


queries = [3, 1, 2, 1]
m = 5
ans = Solution().processQueries(queries, m)
print(ans)

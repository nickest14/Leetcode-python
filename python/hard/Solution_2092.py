# 2092. Find All People With Secret

from typing import List


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            parent[find(b)] = find(a)

        meetings.sort(key=lambda x: x[2])
        union(0, firstPerson)

        i = 0
        while i < len(meetings):
            time: int = meetings[i][2]
            involved: list[int] = []

            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                union(x, y)
                involved.append(x)
                involved.append(y)
                i += 1

            root0 = find(0)
            for p in involved:
                if find(p) != root0:
                    parent[p] = p

        return [i for i in range(n) if find(i) == find(0)]


ans = Solution().findAllPeople(6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1)
print(ans)

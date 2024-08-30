# 947. Most Stones Removed with Same Row or Column

from typing import List
from collections import defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def remove_point(x, y):
            points.discard((x, y))
            for b in x_dic[x]:
                if (x, b) in points:
                    remove_point(x, b)
            for a in y_dic[y]:
                if (a, y) in points:
                    remove_point(a, y)

        x_dic = defaultdict(list)
        y_dic = defaultdict(list)
        points: set[tuple[int, int]] = {(i, j) for i, j in stones}

        for i, j in stones:
            x_dic[i].append(j)
            y_dic[j].append(i)

        count: int = 0
        for i, j in stones:
            if (i, j) in points:
                remove_point(i, j)
                count += 1

        return len(stones) - count


ans = Solution().removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]])
print(ans)

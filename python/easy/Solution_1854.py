# 1854. Maximum Population Year


from typing import List
import operator


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        mn = min(map(operator.itemgetter(0), logs))
        mx = max(map(operator.itemgetter(1), logs))
        intervals = {year: 0 for year in range(mn - 1, mx + 1)}
        for b, d in logs:
            intervals[b] += 1
            intervals[d] -= 1

        earliest = mn - 1
        for y in range(mn, mx + 1):
            intervals[y] += intervals[y - 1]
            if intervals[y] > intervals[earliest]:
                earliest = y
        return earliest


ans = Solution().maximumPopulation([[1993, 1999], [2000, 2010]])
print(ans)

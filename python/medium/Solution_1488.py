# 1488. Avoid Flood in The City

from typing import List
from bisect import bisect_right


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n: int = len(rains)
        ans: List[int] = [1] * n
        last: dict[int, int] = {}
        dry: List[int] = []
        for i, x in enumerate(rains):
            if x == 0:
                dry.append(i)
            else:
                ans[i] = -1
                if x in last:
                    j = bisect_right(dry, last[x])
                    if j == len(dry):
                        return []
                    ans[dry[j]] = x
                    dry.pop(j)
                last[x] = i
        return ans


ans = Solution().avoidFlood([1, 2, 3, 4, 0, 3])
print(ans)

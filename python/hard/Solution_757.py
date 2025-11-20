# 757. Set Intersection Size At Least Two

from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n: int = len(intervals)
        prev1: int = intervals[0][1] - 1
        prev2: int = intervals[0][1]

        ans: int = 2
        for i in range(1, n):
            if prev2 < intervals[i][0]:
                prev1 = intervals[i][1] - 1
                prev2 = intervals[i][1]
                ans += 2
            elif prev1 < intervals[i][0]:
                if intervals[i][1] == prev2:
                    prev1 = intervals[i][1] - 1
                else:
                    prev1 = intervals[i][1]
                prev1, prev2 = min(prev1, prev2), max(prev1, prev2)
                ans += 1
        return ans


ans = Solution().intersectionSizeTwo([[1, 3], [3, 7], [8, 9]])
print(ans)

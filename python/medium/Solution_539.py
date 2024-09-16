# 539. Minimum Time Difference
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times: list[int] = []
        for time in timePoints:
            times.append(60 * int(time[0:2]) + int(time[3:5]))

        times.sort()
        ans: int = 1440 - (times[-1] - times[0])
        for i in range(1, len(times)):
            ans = min(ans, times[i] - times[i - 1])

        return ans


ans = Solution().findMinDifference(["23:59", "00:00"])
print(ans)

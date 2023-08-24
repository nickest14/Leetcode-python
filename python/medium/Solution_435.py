# 435. Non-overlapping Intervals

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort()
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                ans += 1
                prev_end = min(end, prev_end)
        return ans


ans = Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])

print(ans)

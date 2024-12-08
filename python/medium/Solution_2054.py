# 2054. Two Best Non-Overlapping Events

from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        event_points: list[tuple] = []  # (time, is_start, value)
        ans: int = 0
        prev_max: int = 0
        for start, end, val in events:
            event_points.append((start, True, val))
            event_points.append((end + 1, False, val))

        event_points.sort(key=lambda x: (x[0], x[1]))

        for _, is_start, val in event_points:
            if is_start:
                ans = max(ans, prev_max + val)
            else:
                prev_max = max(prev_max, val)

        return ans


ans = Solution().maxTwoEvents([[1, 3, 2], [4, 5, 2], [2, 4, 3]])
print(ans)

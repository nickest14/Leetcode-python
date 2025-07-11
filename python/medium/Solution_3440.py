# 3440. Reschedule Meetings for Maximum Free Time II

from typing import List


class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        n: int = len(startTime)
        if n == 0:
            return eventTime

        gaps: list[int] = [0] * (n + 1)
        gaps[0] = startTime[0]

        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]
        gaps[n] = eventTime - endTime[n - 1]

        largest_right: list[int] = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            largest_right[i] = max(largest_right[i + 1], gaps[i + 1])

        ans: int = 0
        largest_left: int = 0

        for i in range(1, n + 1):
            duration = endTime[i - 1] - startTime[i - 1]
            can_fit_left = largest_left >= duration
            can_fit_right = largest_right[i] >= duration

            if can_fit_left or can_fit_right:
                merged = gaps[i - 1] + gaps[i] + duration
                ans = max(ans, merged)

            ans = max(ans, gaps[i - 1] + gaps[i])
            largest_left = max(largest_left, gaps[i - 1])

        return ans


ans = Solution().maxFreeTime(5, [1, 3], [2, 5])
print(ans)

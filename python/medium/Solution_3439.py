# 3439. Reschedule Meetings for Maximum Free Time I

from typing import List


class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        count: int = len(startTime)
        prefix_sum: list[int] = [0] * (count + 1)
        ans: int = 0

        for i in range(count):
            prefix_sum[i + 1] = prefix_sum[i] + (endTime[i] - startTime[i])

        for i in range(k - 1, count):
            occupied = prefix_sum[i + 1] - prefix_sum[i - k + 1]
            window_end = eventTime if i == count - 1 else startTime[i + 1]
            window_start = 0 if i == k - 1 else endTime[i - k]
            free_time = window_end - window_start - occupied
            ans = max(ans, free_time)

        return ans


ans = Solution().ansTime(5, 1, [1, 3], [2, 5])
print(ans)


print(ans)

# 3169. Count Days Without Meetings

from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days

        meetings.sort(key=lambda x: x[0])

        m_meetings = []
        cur_start, cur_end = meetings[0]
        for start, end in meetings[1:]:
            if start <= cur_end:
                cur_end = max(cur_end, end)
            else:
                m_meetings.append([cur_start, cur_end])
                cur_start, cur_end = start, end
        m_meetings.append([cur_start, cur_end])

        meeting_days = 0
        for start, end in m_meetings:
            meeting_days += (end - start + 1)

        return days - meeting_days

    # def countDays(self, days: int, meetings: List[List[int]]) -> int:
    #     ans = [1] * (days + 1)
    #     for m in meetings:
    #         start, end = m[0], m[1]
    #         for i in range(start, end + 1):
    #             ans[i] = 0

    #     return len([v for v in ans[1:] if v == 1])


days = 10
meetings = [[5, 7], [1, 3], [9, 10]]
ans = Solution().countDays(days, meetings)
print(ans)

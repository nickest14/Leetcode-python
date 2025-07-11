# 2402. Meeting Rooms III

from typing import List
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        free_rooms = list(range(n))
        heapq.heapify(free_rooms)

        busy: list[tuple[int, int]] = []
        count: list[int] = [0] * n

        for start, end in meetings:
            duration = end - start

            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(free_rooms, room)

            if free_rooms:
                room = heapq.heappop(free_rooms)
                count[room] += 1
                heapq.heappush(busy, (end, room))
            else:
                free_time, room = heapq.heappop(busy)
                count[room] += 1
                heapq.heappush(busy, (free_time + duration, room))

        max_meetings = max(count)
        for i, c in enumerate(count):
            if c == max_meetings:
                return i


ans = Solution().mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]])
print(ans)

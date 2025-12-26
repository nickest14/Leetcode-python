# 2040. Kth Smallest Product of Two Sorted Arrays

from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        free_rooms: list[int] = list(range(n))
        heapify(free_rooms)

        busy: list[tuple[int, int]] = []
        count: list[int] = [0] * n

        for start, end in meetings:
            duration: int = end - start

            while busy and busy[0][0] <= start:
                _, room = heappop(busy)
                heappush(free_rooms, room)

            if free_rooms:
                room: int = heappop(free_rooms)
                count[room] += 1
                heappush(busy, (end, room))
            else:
                free_time, room = heappop(busy)
                count[room] += 1
                heappush(busy, (free_time + duration, room))

        max_meetings = max(count)
        for i, c in enumerate(count):
            if c == max_meetings:
                return i


ans = Solution().mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]])
print(ans)
